from src.widget import mask_account_card


def test_mask_card():
    result = mask_account_card("1234567890123456")
    assert result == "1234 56** **** 3456"


def test_mask_account():
    result = mask_account_card("12345678901234567890")
    assert result.startswith("**")


def test_invalid_input():
    result = mask_account_card("123")
    assert result == "123"


def test_widget_account_full():
    result = mask_account_card("12345678901234567890")
    assert result == "**7890"


def test_widget_other_length():
    result = mask_account_card("12345")
    assert result == "12345"


def test_widget_other():
    assert mask_account_card("12345") == "12345"


def test_widget_int_input():
    result = mask_account_card(1234567890123456)
    assert result == "1234 56** **** 3456"


def test_widget_empty():
    result = mask_account_card("")
    assert result == ""
