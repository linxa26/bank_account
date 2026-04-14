import pytest

from src.generators import filter_by_currency


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
            [
                {"operationAmount": {"currency": {"code": "USD"}}},
                {"operationAmount": {"currency": {"code": "EUR"}}},
            ],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        (
            [
                {"operationAmount": {"currency": {"code": "EUR"}}},
                {"operationAmount": {"currency": {"code": "EUR"}}},
            ],
            "USD",
            [],
        ),
        ([], "USD", []),
    ],
)
def test_filter_by_currency(transactions, currency, expected):
    result = list(filter_by_currency(transactions, currency))
    assert result == expected
