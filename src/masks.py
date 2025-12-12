def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Формат результата:
    XXXX XX** **** XXXX

    Принимает номер карты в виде строки или числа.
    """
    card_number = str(card_number)

    """
    Выделяются первые 6 и последние 4 цифры номера карты.
    """
    first_6 = card_number[:6]
    last_4 = card_number[-4:]

    """
    Средняя часть номера заменяется символами "*".
    Количество звездочек определяется длиной номера карты.
    """
    middle_len = len(card_number) - 10
    middle_mask = "*" * middle_len

    """
    Собирается замаскированная строка из частей номера.
    """
    masked = first_6 + middle_mask + last_4

    """
    Результат разбивается на блоки по 4 символа.
    """
    blocks = [masked[i: i + 4] for i in range(0, len(masked), 4)]
    return " ".join(blocks)


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Формат результата:
    **XXXX

    Отображаются только последние 4 цифры номера счета.
    """
    account_number = str(account_number)
    return "**" + account_number[-4:]
