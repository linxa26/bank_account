import re

from src.file_readers import read_csv_transactions, read_excel_transactions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date


def format_account(account: str) -> str:
    """Маскирует номер карты или счёта."""

    if not account:
        return "Не указан"

    if account.startswith("Счет "):
        return f"Счет {get_mask_account(account.split()[-1])}"

    parts = account.rsplit(" ", 1)

    if len(parts) == 2:
        name, number = parts
        return f"{name} {get_mask_card_number(number)}"

    return account


def ask_yes_no(question: str) -> bool:
    """Запрашивает ответ Да или Нет."""

    while True:
        answer = input(question).strip().lower()

        if answer in ("да", "нет"):
            return answer == "да"

        print("Введите Да или Нет.")


def main() -> None:
    """Запускает программу обработки банковских транзакций."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            transactions = load_transactions("operations.json")
            break

        elif choice == "2":
            transactions = read_csv_transactions("src/data/transactions.csv")
            break

        elif choice == "3":
            transactions = read_excel_transactions("src/data/transactions_excel.xlsx")
            break

        else:
            print("Неверный пункт меню. Попробуйте снова.")

    if not transactions:
        print("Не удалось получить транзакции из файла.")
        return

    # Фильтрация по статусу
    valid_statuses = ("EXECUTED", "CANCELED", "PENDING")

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные статусы: EXECUTED, CANCELED, PENDING")

        status = input("Ваш статус: ").strip().upper()

        if status in valid_statuses:
            break

        print(f'Статус операции "{status}" недоступен.')

    transactions = filter_by_state(transactions, status)

    print(f'Операции отфильтрованы по статусу "{status}".')

    # Сортировка по дате
    if ask_yes_no("\nОтсортировать операции по дате? Да/Нет: "):

        while True:
            order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()

            if order in ("по возрастанию", "по убыванию"):
                break

            print("Введите 'по возрастанию' или 'по убыванию'.")

        transactions = sort_by_date(transactions, reverse=(order == "по убыванию"))

    # Фильтрация по валюте
    if ask_yes_no("\nВыводить только рублёвые транзакции? Да/Нет: "):

        transactions = [
            transaction
            for transaction in transactions
            if (
                transaction.get("currency_code")
                or transaction.get("operationAmount", {}).get("currency", {}).get("code")
            )
            == "RUB"
        ]

    # Фильтрация по описанию
    if ask_yes_no("\nОтфильтровать список транзакций по слову в описании? Да/Нет: "):

        search_word = input("Введите слово для поиска: ").strip()

        transactions = [
            transaction
            for transaction in transactions
            if re.search(
                re.escape(search_word),
                str(transaction.get("description", "")),
                re.IGNORECASE,
            )
        ]

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")

    if not transactions:
        print("Не найдено ни одной транзакции, " "подходящей под ваши условия фильтрации.")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:

        date = get_date(str(transaction.get("date", "")))
        description = transaction.get("description", "Без описания")

        amount = transaction.get("amount", transaction.get("operationAmount", {}).get("amount", 0))

        currency = transaction.get(
            "currency_name", transaction.get("operationAmount", {}).get("currency", {}).get("name", "")
        )

        sender = format_account(str(transaction.get("from", "")))
        receiver = format_account(str(transaction.get("to", "")))

        print()
        print(f"{date} {description}")
        print(f"{sender} -> {receiver}")
        print(f"Сумма: {amount} {currency}")


if __name__ == "__main__":
    main()
