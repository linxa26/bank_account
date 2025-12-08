def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате:
    XXXX XX** **** XXXX
    """
    # Убедимся, что передан строковый тип
    card_number = str(card_number)

    # Получаем части
    first_6 = card_number[:6]
    last_4 = card_number[-4:]

    # Середина — маскируем
    middle_len = len(card_number) - 10  # сколько звездочек нужно
    middle_mask = "*" * middle_len

    # Собираем
    masked = first_6 + middle_mask + last_4

    # Разбиваем на блоки по 4
    blocks = [masked[i: i + 4] for i in range(0, len(masked), 4)]
    return " ".join(blocks)


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX
    """
    account_number = str(account_number)
    return "**" + account_number[-4:]
