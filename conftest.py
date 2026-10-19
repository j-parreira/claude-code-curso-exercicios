# conftest.py — Shared pytest fixtures for tests/ and exercises/checks/

import pytest

from todo.cli import main


@pytest.fixture
def todo(tmp_path, monkeypatch, capsys):
    """Return a runner for the CLI against a temporary task file.

    The runner takes the arguments of one command and returns (exit code, stdout).
    """
    monkeypatch.setenv("TODO_FILE", str(tmp_path / "tasks.json"))

    def run(*argv: str) -> tuple[int, str]:
        code = main(list(argv))
        return code, capsys.readouterr().out

    return run
