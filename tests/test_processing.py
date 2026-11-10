import pytest

from src.processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)


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


def test_filter_empty():
    result = filter_by_state([], "EXECUTED")
    assert result == []


def test_sort_by_date_desc(operations):
    result = sort_by_date(operations, reverse=True)
    assert result[0]["date"] == "2023-06-01"


def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, reverse=False)
    assert result[0]["date"] == "2023-04-01"


def test_process_bank_operations():
    """Проверяет подсчёт операций по категориям."""
    data = [
        {"description": "Перевод"},
        {"description": "Оплата"},
        {"description": "Перевод"},
    ]
    categories = ["Перевод"]

    result = process_bank_operations(data, categories)

    assert result == {"Перевод": 2}


def test_process_bank_search():
    """Проверяет поиск операций по описанию."""
    data = [
        {"description": "Перевод"},
        {"description": "Оплата"},
        {"description": "Перевод"},
    ]

    result = process_bank_search(data, "Перевод")

    assert result == [
        {"description": "Перевод"},
        {"description": "Перевод"},
    ]
