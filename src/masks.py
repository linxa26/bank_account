def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Формат результата: XXXX XX** **** XXXX
    """
    card_number = str(card_number)

    first_6 = card_number[:6]
    last_4 = card_number[-4:]

    middle_len = len(card_number) - 10
    middle_mask = "*" * middle_len

    masked_number = first_6 + middle_mask + last_4

    blocks = [masked_number[i : i + 4] for i in range(0, len(masked_number), 4)]

    return " ".join(blocks)


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта.

    Формат результата: **XXXX
    """
    account_number = str(account_number)
    return "**" + account_number[-4:]
