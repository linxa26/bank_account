import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("12345678901234567890", "**7890"),
        ("00000000000000000001", "**0001"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
