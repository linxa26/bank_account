import pytest
from src.decorators import log


def test_success(capsys):
    @log()
    def f():
        return 1

    f()

    captured = capsys.readouterr()

    assert "ok" in captured.out


def test_error(capsys):
    @log()

    def f():
        return 1 / 0

    with pytest.raises(ZeroDivisionError):
        f()

    captured = capsys.readouterr()

    assert "error" in captured.out
