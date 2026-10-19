# query.py — Filter and sort tasks for the list command

from datetime import date

from todo.models import PRIORITIES, Task

SORT_KEYS = ("id", "due", "priority")


def pending(tasks: list[Task]) -> list[Task]:
    """Return the tasks not yet done."""
    return [task for task in tasks if not task.done]


def overdue(tasks: list[Task], today: date) -> list[Task]:
    """Return the pending tasks whose due date has passed."""
    return [
        task
        for task in tasks
        if not task.done and task.due is not None and task.due <= today
    ]


def sort_tasks(tasks: list[Task], key: str) -> list[Task]:
    """Return tasks sorted by key: id, due (undated last) or priority (highest first)."""
    if key == "id":
        return sorted(tasks, key=lambda task: task.id)
    if key == "due":
        return sorted(tasks, key=lambda task: (task.due is None, task.due or date.max))
    if key == "priority":
        return sorted(tasks, key=lambda task: PRIORITIES.index(task.priority))
    raise ValueError(f"unknown sort key: {key}")
