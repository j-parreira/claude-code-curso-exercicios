# storage.py — Load and save the task list as a JSON file

import json
import os
from pathlib import Path

from todo.models import Task

DEFAULT_FILE = "tasks.json"


def data_file() -> Path:
    """Return the task file path: $TODO_FILE, or tasks.json in the current directory."""
    return Path(os.environ.get("TODO_FILE", DEFAULT_FILE))


def load(path: Path) -> list[Task]:
    """Read all tasks from path; a missing file means no tasks yet."""
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Task.from_dict(item) for item in raw]


def save(path: Path, tasks: list[Task]) -> None:
    """Write all tasks to path, replacing its contents."""
    text = json.dumps([task.to_dict() for task in tasks], indent=2)
    path.write_text(text + "\n", encoding="utf-8")


def next_id(tasks: list[Task]) -> int:
    """Return the id for a new task."""
    return len(tasks) + 1
