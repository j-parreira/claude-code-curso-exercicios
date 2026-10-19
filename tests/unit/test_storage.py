# test_storage.py — Tests for loading and saving the task file

from todo import storage
from todo.models import Task


def test_missing_file_means_no_tasks(tmp_path):
    assert storage.load(tmp_path / "nothing.json") == []


def test_save_then_load_returns_the_same_tasks(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [Task(id=1, title="a"), Task(id=2, title="b", done=True)]
    storage.save(path, tasks)
    assert storage.load(path) == tasks


def test_data_file_follows_the_environment(monkeypatch, tmp_path):
    monkeypatch.setenv("TODO_FILE", str(tmp_path / "mine.json"))
    assert storage.data_file() == tmp_path / "mine.json"


def test_first_id_is_one():
    assert storage.next_id([]) == 1


def test_next_id_follows_the_last_task():
    assert storage.next_id([Task(id=1, title="a"), Task(id=2, title="b")]) == 3
