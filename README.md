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
<!-- Pull request submission -->
