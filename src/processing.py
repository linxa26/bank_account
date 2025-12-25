def filter_by_state(operations, state="EXECUTED"):
    """
    Фильтрует список операций по значению ключа state.
    """
    return [
        operation for operation in operations
        if operation.get("state") == state
    ]


def sort_by_date(operations, reverse=True):
    """
    Сортирует список операций по дате.
    """
    return sorted(
        operations,
        key=lambda operation: operation.get("date", ""),
        reverse=reverse
    )
