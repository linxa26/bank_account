import pytest

from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "transactions, expected",
    [
        ([{"description": "Перевод"}], ["Перевод"]),
        ([{"description": "Покупка"}, {"description": "Оплата"}], ["Покупка", "Оплата"]),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected
