# test_legacy_import.py — Smoke test for the old todo.txt importer

from datetime import date

from todo.legacy_import import importFile


def test_imports_a_simple_file(tmp_path):
    path = tmp_path / "todo.txt"
    path.write_text("(A) Pay rent due:2026-11-01\nBuy milk\n", encoding="utf-8")
    assert importFile(path) == [
        {
            "done": False,
            "priority": "high",
            "due": date(2026, 11, 1),
            "title": "Pay rent",
        },
        {"done": False, "priority": "medium", "due": None, "title": "Buy milk"},
    ]
