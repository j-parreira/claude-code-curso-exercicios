# cli.py — Command-line interface: argument parsing and command dispatch

import argparse
import sys
from datetime import date
from pathlib import Path

from todo import legacy_import, query, storage
from todo.models import PRIORITIES, Task


class TaskNotFound(Exception):
    pass


def build_parser() -> argparse.ArgumentParser:
    """Return the parser for every todo subcommand."""
    parser = argparse.ArgumentParser(prog="todo", description="A small task tracker.")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a task")
    add.add_argument("title")
    add.add_argument("--priority", choices=PRIORITIES, default="medium")
    add.add_argument("--due", type=date.fromisoformat, help="due date, YYYY-MM-DD")

    show = sub.add_parser("list", help="list pending tasks")
    show.add_argument("--all", action="store_true", help="include done tasks")
    show.add_argument(
        "--overdue",
        action="store_true",
        help="only pending tasks whose due date has passed",
    )
    show.add_argument(
        "--sort",
        choices=query.SORT_KEYS,
        default="id",
        help="sort order (default: id); priority puts the highest first",
    )

    for name, text in (("done", "mark a task as done"), ("rm", "remove a task")):
        sub.add_parser(name, help=text).add_argument("id", type=int)

    old = sub.add_parser("import", help="import tasks from an old todo.txt export")
    old.add_argument("file", type=Path)
    return parser


def format_task(task: Task) -> str:
    """Return the one-line form of a task used by list."""
    mark = "x" if task.done else " "
    due = f"  due {task.due.isoformat()}" if task.due else ""
    return f"[{mark}] {task.id:>3}  {task.title}  ({task.priority}){due}"


def find(tasks: list[Task], task_id: int) -> Task:
    """Return the task with task_id, or raise TaskNotFound."""
    for task in tasks:
        if task.id == task_id:
            return task
    raise TaskNotFound(f"no task with id {task_id}")


def cmd_add(args: argparse.Namespace, tasks: list[Task]) -> bool:
    task = Task(
        id=storage.next_id(tasks),
        title=args.title,
        priority=args.priority,
        due=args.due,
    )
    tasks.append(task)
    print(f"added {task.id}")
    return True


def cmd_list(args: argparse.Namespace, tasks: list[Task]) -> bool:
    shown = tasks if args.all else query.pending(tasks)
    if args.overdue:
        shown = query.overdue(shown, date.today())
    for task in query.sort_tasks(shown, args.sort):
        print(format_task(task))
    return False


def cmd_done(args: argparse.Namespace, tasks: list[Task]) -> bool:
    find(tasks, args.id).done = True
    print(f"done {args.id}")
    return True


def cmd_rm(args: argparse.Namespace, tasks: list[Task]) -> bool:
    tasks.remove(find(tasks, args.id))
    print(f"removed {args.id}")
    return True


def cmd_import(args: argparse.Namespace, tasks: list[Task]) -> bool:
    items = legacy_import.importFile(args.file)
    for item in items:
        tasks.append(Task(id=storage.next_id(tasks), **item))
    print(f"imported {len(items)}")
    return True


# Each command returns True when it changed the task list, so main knows to save.
COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "done": cmd_done,
    "rm": cmd_rm,
    "import": cmd_import,
}


def main(argv: list[str] | None = None) -> int:
    """Run one todo command; return the process exit code."""
    args = build_parser().parse_args(argv)
    path = storage.data_file()
    tasks = storage.load(path)
    try:
        changed = COMMANDS[args.command](args, tasks)
    except TaskNotFound as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if changed:
        storage.save(path, tasks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
