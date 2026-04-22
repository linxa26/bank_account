import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-06-01"},
        {"id": 2, "state": "CANCELLED", "date": "2023-04-01"},
        {"id": 3, "state": "EXECUTED", "date": "2023-05-01"},
    ]


def test_filter_by_state(operations):
    result = filter_by_state(operations, "EXECUTED")
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


def test_filter_empty(operations):
    result = filter_by_state([], "EXECUTED")
    assert result == []


def test_sort_by_date_desc(operations):
    result = sort_by_date(operations, reverse=True)
    assert result[0]["date"] == "2023-06-01"


def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, reverse=False)
    assert result[0]["date"] == "2023-04-01"
