# test_s04.py — Verification for session 4: the three reported bugs, and tests for query.py

from datetime import date, timedelta
from pathlib import Path

from todo import query
from todo.models import Task

ROOT = Path(__file__).resolve().parents[2]
TODAY = date(2026, 11, 10)


def test_an_id_never_belongs_to_two_tasks(todo):
    todo("add", "a")
    todo("add", "b")
    todo("rm", "1")
    todo("add", "c")
    ids = [line.split()[2] for line in todo("list")[1].splitlines()]
    assert sorted(ids) == sorted(set(ids))


def test_a_task_due_today_is_not_overdue():
    assert query.overdue([Task(id=1, title="a", due=TODAY)], TODAY) == []


def test_a_task_due_yesterday_is_overdue():
    task = Task(id=1, title="a", due=TODAY - timedelta(days=1))
    assert query.overdue([task], TODAY) == [task]


def test_sort_by_priority_puts_the_highest_first(todo):
    for priority in ("low", "high", "medium"):
        todo("add", priority, "--priority", priority)
    titles = [
        line.split()[3] for line in todo("list", "--sort", "priority")[1].splitlines()
    ]
    assert titles == ["high", "medium", "low"]


def test_query_module_has_tests():
    assert (ROOT / "tests" / "unit" / "test_query.py").exists()
