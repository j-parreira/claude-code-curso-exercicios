# models.py — The Task record and its JSON-compatible dict form

from dataclasses import dataclass
from datetime import date

PRIORITIES = ("low", "medium", "high")


@dataclass
class Task:
    id: int
    title: str
    priority: str = "medium"
    due: date | None = None
    done: bool = False

    def to_dict(self) -> dict:
        """Return the task as a dict that json.dumps can write."""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due": self.due.isoformat() if self.due else None,
            "done": self.done,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Build a task from the dict written by to_dict."""
        return cls(
            id=data["id"],
            title=data["title"],
            priority=data["priority"],
            due=date.fromisoformat(data["due"]) if data["due"] else None,
            done=data["done"],
        )
