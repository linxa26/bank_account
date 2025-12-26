from typing import List, Dict


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по значению ключа 'state'.

    :param operations: список операций
    :param state: статус операции для фильтрации
    :return: отфильтрованный список операций
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param operations: список операций
    :param reverse: порядок сортировки (по умолчанию — по убыванию)
    :return: отсортированный список операций
    """
    return sorted(operations, key=lambda operation: operation.get("date", ""), reverse=reverse)
