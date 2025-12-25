from src.widget import mask_account_card, get_date
from processing import filter_by_state, sort_by_date


if __name__ == "__main__":
    print(mask_account_card("1234567890123456"))
    print(get_date("2024-03-11T02:26:18.671407"))

    data = [
        {"id": 1, "state": "EXECUTED", "date": "2023-06-01"},
        {"id": 2, "state": "CANCELED", "date": "2023-04-01"},
        {"id": 3, "state": "EXECUTED", "date": "2023-05-01"},
    ]

    print(filter_by_state(data))
    print(sort_by_date(data))
