# test_cli.py — Tests for the todo commands, run end to end against a temporary file


def test_add_then_list(todo):
    assert todo("add", "Write report", "--priority", "high") == (0, "added 1\n")
    code, out = todo("list")
    assert code == 0
    assert "Write report" in out
    assert "(high)" in out


def test_list_shows_the_due_date(todo):
    todo("add", "Pay rent", "--due", "2026-11-01")
    assert "due 2026-11-01" in todo("list")[1]


def test_done_tasks_are_hidden_unless_all(todo):
    todo("add", "a")
    todo("add", "b")
    todo("done", "1")
    assert "a" not in todo("list")[1].split()
    assert "[x]" in todo("list", "--all")[1]


def test_rm_removes_the_task(todo):
    todo("add", "a")
    todo("rm", "1")
    assert todo("list")[1] == ""


def test_unknown_id_is_an_error(todo):
    assert todo("done", "7")[0] == 1


def test_sort_by_due_puts_undated_last(todo):
    todo("add", "undated")
    todo("add", "later", "--due", "2026-12-01")
    todo("add", "sooner", "--due", "2026-11-01")
    titles = [line.split()[3] for line in todo("list", "--sort", "due")[1].splitlines()]
    assert titles == ["sooner", "later", "undated"]
