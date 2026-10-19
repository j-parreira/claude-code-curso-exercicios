# test_s03.py — Verification for session 3: export command and the project CLAUDE.md

import csv
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _two_tasks(todo):
    todo("add", "Pay rent", "--priority", "high", "--due", "2026-11-01")
    todo("add", "Buy milk, eggs")
    todo("done", "2")


def test_markdown_export_lists_every_task(todo):
    _two_tasks(todo)
    code, out = todo("export", "--format", "md")
    assert code == 0
    assert out.splitlines() == ["- [ ] Pay rent", "- [x] Buy milk, eggs"]


def test_markdown_is_the_default_format(todo):
    _two_tasks(todo)
    assert todo("export")[1] == todo("export", "--format", "md")[1]


def test_csv_export(todo):
    _two_tasks(todo)
    rows = list(csv.reader(io.StringIO(todo("export", "--format", "csv")[1])))
    assert rows == [
        ["id", "title", "priority", "due", "done"],
        ["1", "Pay rent", "high", "2026-11-01", "false"],
        ["2", "Buy milk, eggs", "medium", "", "true"],
    ]


def test_export_to_a_file(todo, tmp_path):
    _two_tasks(todo)
    target = tmp_path / "out.md"
    code, out = todo("export", "--output", str(target))
    assert code == 0
    assert out == ""
    assert target.read_text(encoding="utf-8").splitlines()[0] == "- [ ] Pay rent"


def test_claude_md_names_the_test_command():
    claude_md = ROOT / "CLAUDE.md"
    assert claude_md.exists(), "CLAUDE.md is missing at the repository root"
    assert "uv run pytest" in claude_md.read_text(encoding="utf-8")
