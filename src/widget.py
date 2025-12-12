from masks import get_mask_card_number, get_mask_account


def mask_account_card(number: str) -> str:
    """
    Определяет тип входного номера и возвращает замаскированное значение.

    Функция принимает номер банковской карты или номер счёта,
    определяет их тип по длине строки и передаёт номер
    в соответствующую функцию маскирования.

    Логика работы:
    если длина номера равна 16 символам - номер считается номером карты;
    если длина номера равна 20 символам - номер считается номером счёта;
    в остальных случаях функция возвращает исходное значение без изменений.

    Маскирование выполняется с помощью функций из модуля masks.
    """
    number = str(number)
    number_len = len(number)

    if number_len == 16:
        return get_mask_card_number(number)

    if number_len == 20:
        return get_mask_account(number)

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
