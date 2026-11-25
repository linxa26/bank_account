import re
from collections import Counter


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по значению ключа state.
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список операций по дате.
    """
    return sorted(operations, key=lambda operation: operation.get("date", ""), reverse=reverse)


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """Подсчитывает количество банковских операций по заданным категориям"""
    names = []
    for i in data:
        if i["description"] in categories:
            names.append(i["description"])
    counts = dict(Counter(names))
    return counts


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Ищет банковские операции по описанию."""
    result = []
    for i in data:
        description = i.get("description", "")
        if re.search(search, description, re.IGNORECASE):
            result.append(i)
    return result
