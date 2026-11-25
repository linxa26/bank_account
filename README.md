
# Учебный проект bank_account

Учебный проект на Python для работы с банковскими операциями.

Проект демонстрирует работу с модулями, функциями, списками словарей, чтением файлов CSV, Excel и JSON, генераторами, регулярными выражениями, декораторами, объектно-ориентированным программированием (ООП) и автоматическим тестированием.

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
- `src/product.py` — классы Product и Category для работы с товарами и категориями.

Тесты находятся в папке `tests/`.

## Установка зависимостей

При использовании Poetry выполните в корне проекта:

```bash
poetry install
```

Для работы с Excel необходимы библиотеки `pandas` и `openpyxl`, указанные в зависимостях проекта.

## Модуль processing

Модуль содержит функции для фильтрации, сортировки и поиска банковских операций.

### filter_by_state

Фильтрует список операций по значению ключа `state`.

По умолчанию возвращаются операции со статусом `EXECUTED`.

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

Сортирует операции по значению ключа `date`.

По умолчанию используется сортировка по убыванию даты.

### process_bank_operations

Подсчитывает количество операций по указанным категориям, используя поле `description`.

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

Ищет операции по тексту в поле `description`.

Поиск выполняется с помощью регулярных выражений без учёта регистра. Возвращает список подходящих операций.

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

Принимает путь к CSV-файлу и возвращает список словарей с транзакциями.

Для чтения используется стандартная библиотека `csv`, разделитель полей — `;`.

### read_excel_transactions(file_path)

Принимает путь к Excel-файлу формата `.xlsx` и возвращает список словарей с транзакциями.

Для чтения используется библиотека `pandas`.

### Пример использования

Замените пути на пути к вашим файлам:

```python
from src.file_readers import read_csv_transactions, read_excel_transactions

csv_transactions = read_csv_transactions("путь/к/файлу.csv")
excel_transactions = read_excel_transactions("путь/к/файлу.xlsx")

print(csv_transactions[:2])
print(excel_transactions[:2])
```

## Объектно-ориентированное программирование (ООП)

В модуле `src/product.py` реализованы два класса: `Product` и `Category`.

Классы позволяют создавать объекты товаров, объединять товары в категории и вести подсчёт созданных категорий и товаров.

### Класс Product

Класс `Product` представляет отдельный товар.

При создании объекта передаются четыре атрибута:

- `name` (`str`) — название товара.
- `description` (`str`) — описание товара.
- `price` (`float`) — цена товара.
- `quantity` (`int`) — количество товара на складе.

Атрибуты инициализируются с помощью метода `__init__`.

Пример создания объекта:

```python
from src.product import Product

phone = Product("Samsung", "Смартфон", 50000.0, 10)

print(phone.name)       # Samsung
print(phone.price)      # 50000.0
print(phone.quantity)   # 10
```

### Класс Category

Класс `Category` представляет категорию товаров.

Он содержит три атрибута:

- `name` (`str`) — название категории.
- `description` (`str`) — описание категории.
- `products` (`list[Product]`) — список объектов класса Product.

Также реализованы два атрибута класса:

- `category_count` — общее количество созданных категорий.
- `product_count` — общее количество товаров, переданных в категории при их создании.

Счётчики увеличиваются автоматически при создании нового объекта `Category`.

Для подсчёта товаров используется функция `len(products)`.

### Пример использования Product и Category

```python
from src.product import Product, Category

# Создание товаров
phone = Product("Samsung", "Смартфон", 50000.0, 10)
iphone = Product("iPhone", "Смартфон", 80000.0, 5)

# Создание категории
category = Category(
    "Смартфоны",
    "Мобильные телефоны",
    [phone, iphone]
)

# Получение информации о категории
print(category.name)
print(category.description)

# Количество товаров в категории
print(len(category.products))

# Цена первого товара
print(category.products[0].price)

# Счётчики классов
print(Category.category_count)
print(Category.product_count)
```

Результат выполнения при запуске примера отдельно:

```text
Смартфоны
Мобильные телефоны
2
50000.0
1
2
```

Список `products` хранит ссылки на объекты класса `Product`.

Если изменить атрибут товара через категорию, изменения будут видны и при обращении к исходному объекту.

Счётчик `product_count` обновляется при создании категории. Изменение списка товаров после создания категории автоматически не обновляет этот счётчик.

## Тестирование

Для тестирования проекта используется библиотека `pytest`.

Тесты располагаются в директории `tests/`.

### Запуск всех тестов

Из корня проекта выполните:

```bash
python -m pytest
```

Последний результат проверки:

```text
43 passed
```

Все тесты проекта успешно пройдены.

### Тестирование классов Product и Category

Для тестирования новых классов используется файл `tests/test_product.py`.

Тесты проверяют:

- Корректное создание объекта Product.
- Сохранение атрибутов товара.
- Создание категории со списком товаров.
- Сохранение атрибутов категории.
- Работу счётчика category_count.
- Работу счётчика product_count.

Запуск тестов:

```bash
python -m pytest tests/test_product.py -v
```

Результат:

```text
4 passed
```

### Проверка покрытия кода

Для проверки покрытия используется `pytest-cov`.

Проверка покрытия модуля `product.py`:

```bash
python -m pytest tests/test_product.py --cov=src.product --cov-report=term-missing
```

Последний результат:

```text
Name             Stmts   Miss  Cover
------------------------------------
src/product.py      21      0   100%
------------------------------------
TOTAL               21      0   100%
```

Покрытие модуля `src/product.py` составляет 100%.

Проверка покрытия всего проекта:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

### Проверка качества кода

Для проверки соответствия стилю PEP 8 используется `flake8`.

```bash
python -m flake8 src/product.py tests/test_product.py
```

Последняя проверка новых файлов завершилась без замечаний.

Проверка форматирования Black:

```bash
python -m black --check src tests
```

Проверка порядка импортов isort:

```bash
python -m isort --profile black --check-only src tests
```

## Используемые технологии

- Python 3.13
- Poetry
- pytest
- pytest-cov
- flake8
- Black
- isort
- pandas
- openpyxl

## Назначение проекта

Проект создан в учебных целях для закрепления навыков программирования на Python.

Основные изучаемые темы:

- Функции и модули.
- Работа со списками и словарями.
- Чтение и обработка файлов.
- Генераторы и декораторы.
- Регулярные выражения.
- Объектно-ориентированное программирование.
- Классы, объекты и методы.
- Атрибуты экземпляров и классов.
- Аннотации типов.
- Автоматическое тестирование с pytest.
- Проверка покрытия кода тестами.
