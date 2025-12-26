from masks import get_mask_card_number, get_mask_account


def mask_account_card(number: str) -> str:
    """
    Определяет тип входного номера и возвращает замаскированное значение.
    """
    number = str(number)

    if len(number) == 16:
        return str(get_mask_card_number(number))

    if len(number) == 20:
        return str(get_mask_account(number))

    return number


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO в формат ДД.ММ.ГГГГ.

    Функция принимает строку с датой и временем в формате:
    YYYY-MM-DDTHH:MM:SS.microseconds

    Возвращает строку, содержащую только дату в формате:
    ДД.ММ.ГГГГ.

    Пример:
    "2024-03-11T02:26:18.671407" → "11.03.2024"
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
