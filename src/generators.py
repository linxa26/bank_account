from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> list:
    """Функция принимает на вход список словарей, представляющих
    транзакции,а возвращает итератор, который поочередно выдает
    транзакции, где валюта операции соответствует заданной"""

    for i in transactions:
        if i.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield i


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for i in transactions:
        yield i.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Функция  приниматет начальное и конечное значения
    для генерации диапазона номеров и выдает номера
    банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты."""
    for number in range(start, stop + 1):
        s = str(number).zfill(16)
        yield " ".join(s[i:i + 4] for i in range(0, 16, 4))


print(list(card_number_generator(5, 2)))
