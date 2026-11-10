
# Учебный проект bank_account

Учебный проект на Python для работы с банковскими операциями. Проект демонстрирует работу с модулями, списками словарей, чтением файлов CSV, Excel и JSON, генераторами, регулярными выражениями и тестированием.

## Структура проекта

Основные файлы находятся в папке `src/`:

- `src/masks.py` — маскирование номеров карт и счетов.
- `src/widget.py` — обработка информации о картах, счетах и датах.
- `src/processing.py` — фильтрация, сортировка и поиск банковских операций, подсчёт операций по категориям.
- `src/generators.py` — генераторы для работы с транзакциями.
- `src/file_readers.py` — чтение транзакций из CSV и Excel.
- `src/utils.py` — загрузка операций из JSON и конвертация валют в рубли.
- `src/decorators.py` — декораторы для логирования.
- `src/main.py` — основная программа.

Тесты находятся в папке `tests/`.

## Установка зависимостей

При использовании Poetry выполните в корне проекта:

```bash
poetry install
```

Для работы с Excel необходимы библиотеки `pandas` и `openpyxl`, указанные в зависимостях проекта.

## Модуль processing

### filter_by_state

Фильтрует список операций по значению ключа `state`. По умолчанию возвращаются операции со статусом `EXECUTED`.

```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"},
]

result = filter_by_state(operations)
print(result)
```

### sort_by_date

Сортирует операции по значению ключа `date`. По умолчанию используется сортировка по убыванию даты.

### process_bank_operations

Подсчитывает количество операций по указанным категориям, используя их `description`.

```python
from src.processing import process_bank_operations

operations = [
    {"description": "Перевод"},
    {"description": "Оплата"},
    {"description": "Перевод"},
]

result = process_bank_operations(operations, ["Перевод"])
print(result)  # {'Перевод': 2}
```

### process_bank_search

Ищет операции по тексту в поле `description`. Поиск выполняется с помощью регулярных выражений без учёта регистра. Возвращает список подходящих операций.

```python
from src.processing import process_bank_search

operations = [
    {"description": "Перевод на карту"},
    {"description": "Оплата телефона"},
]

result = process_bank_search(operations, "перевод")
print(result)  # [{'description': 'Перевод на карту'}]
```

## Модуль generators

Модуль содержит генераторы для обработки транзакций и генерации данных.

### filter_by_currency

Фильтрует транзакции по заданной валюте.

```python
from src.generators import filter_by_currency

transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}},
]

result = list(filter_by_currency(transactions, "USD"))
print(result)
```

## Чтение операций из CSV и Excel

Модуль `src/file_readers.py` содержит функции для загрузки финансовых транзакций.

### read_csv_transactions(file_path)

Принимает путь к CSV-файлу и возвращает список словарей с транзакциями. Для чтения используется стандартная библиотека `csv`, разделитель полей — `;`.

### read_excel_transactions(file_path)

Принимает путь к Excel-файлу формата `.xlsx` и возвращает список словарей с транзакциями. Для чтения используется библиотека `pandas`.

Пример использования (замените пути на пути к вашим файлам):

```python
from src.file_readers import read_csv_transactions, read_excel_transactions

csv_transactions = read_csv_transactions("путь/к/файлу.csv")
excel_transactions = read_excel_transactions("путь/к/файлу.xlsx")

print(csv_transactions[:2])
print(excel_transactions[:2])
```

## Тестирование

Запуск всех тестов из корня проекта:

```bash
python -m pytest
```

Проверка покрытия кода тестами:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

Проверка форматирования Black и порядка импортов isort:

```bash
python -m black --check src tests
python -m isort --profile black --check-only src tests
```
