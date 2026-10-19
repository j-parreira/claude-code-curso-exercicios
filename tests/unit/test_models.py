# test_models.py — Tests for the Task record and its dict form

from datetime import date

from todo.models import Task


def test_round_trip_with_due_date():
    task = Task(id=1, title="Pay rent", priority="high", due=date(2026, 11, 1))
    assert Task.from_dict(task.to_dict()) == task


def test_round_trip_without_due_date():
    task = Task(id=2, title="Buy milk", done=True)
    assert Task.from_dict(task.to_dict()) == task


def test_dict_form_stores_due_as_iso_text():
    assert Task(id=1, title="x", due=date(2026, 1, 5)).to_dict()["due"] == "2026-01-05"
