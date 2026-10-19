# test_s02.py — Verification for session 2: tags on tasks

import json


def test_tags_are_shown_in_list(todo):
    todo("add", "Write report", "--tag", "work", "--tag", "urgent")
    out = todo("list")[1]
    assert "#work" in out
    assert "#urgent" in out


def test_list_filters_by_tag(todo):
    todo("add", "Write report", "--tag", "work")
    todo("add", "Buy milk", "--tag", "home")
    out = todo("list", "--tag", "work")[1]
    assert "Write report" in out
    assert "Buy milk" not in out


def test_tags_ignore_case(todo):
    todo("add", "Write report", "--tag", "Work")
    out = todo("list", "--tag", "WORK")[1]
    assert "Write report" in out
    assert "#work" in out


def test_a_repeated_tag_is_stored_once(todo):
    todo("add", "Write report", "--tag", "work", "--tag", "work")
    assert todo("list")[1].count("#work") == 1


def test_a_file_from_before_tags_still_loads(todo, tmp_path):
    old = [
        {"id": 1, "title": "Old task", "priority": "low", "due": None, "done": False}
    ]
    (tmp_path / "tasks.json").write_text(json.dumps(old), encoding="utf-8")
    code, out = todo("list")
    assert code == 0
    assert "Old task" in out
    assert "#" not in out
