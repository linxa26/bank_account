# Учебный проект bank_account

Учебный проект на Python для работы с банковскими операциями.
Проект демонстрирует базовую архитектуру Python-приложения,
работу с модулями, списками словарей и Git.

## Структура проекта

- `masks.py` — функции для маскирования номеров карт и счетов
- `widget.py` — логика определения типа номера и вызова нужной функции маскирования
- `processing.py` — обработка данных (фильтрация и сортировка операций)
- `main.py` — точка входа и примеры использования функций

## Модуль processing

### filter_by_state

Фильтрует список операций по значению ключа `state`.

По умолчанию возвращаются операции со статусом `EXECUTED`.

```python
from processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"},
]

result = filter_by_state(operations)

<<<<<<< HEAD
## Тесты

Для запуска тестов используйте:

pytest

Для проверки покрытия:

pytest --cov=src

## Модуль generators

Модуль содержит генераторы для обработки транзакций и генерации данных.

---

### filter_by_currency

Фильтрует список транзакций по заданной валюте.

```python
from src.generators import filter_by_currency

transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}},
]

result = list(filter_by_currency(transactions, "USD"))

## Модуль generators

Модуль содержит генераторы для обработки транзакций и генерации данных.

---

### filter_by_currency

Фильтрует список транзакций по заданной валюте.

```python
from src.generators import filter_by_currency

transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}},
]

result = list(filter_by_currency(transactions, "USD"))
=======
## Тестирование

Для запуска тестов используется pytest.

Установка зависимостей:

```bash
poetry install
>>>>>>> e0614641b357ca006ea6cb491d77cadf8995deaf

Чтение финансовых операций из CSV и Excel

В проект добавлен модуль src/file_readers.py, предназначенный для загрузки финансовых транзакций из файлов CSV и Excel.

Функция read_csv_transactions(file_path)

Принимает путь к CSV-файлу, считывает финансовые операции и возвращает список словарей с транзакциями.

Для чтения используется стандартная библиотека csv и разделитель ;.

Функция read_excel_transactions(file_path)

Принимает путь к Excel-файлу формата .xlsx и возвращает список словарей с транзакциями.

Для чтения используется библиотека pandas.

Пример использования

from src.file_readers import read_csv_transactions, read_excel_transactions

csv_transactions = read_csv_transactions("src/data/transactions.csv")
excel_transactions = read_excel_transactions("src/data/transactions_excel.xlsx")

print(csv_transactions[:2])print(excel_transactions[:2])

Для работы с Excel необходимы библиотеки pandas и openpyxl, добавленные в зависимости проекта.