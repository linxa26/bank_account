from pathlib import Path
import json
import logging
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")

if API_KEY is None:
    raise ValueError("EXCHANGE_API_KEY не найден")

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    LOG_DIR / "utils.log",
    mode="w",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(operation: str) -> list:
    """Функция загружает транзакции из JSON-файла"""
    logger.info("Начало загрузки транзакций")

    try:
        with open(
                Path(__file__).parent.parent / "data" / operation,
                encoding="utf-8"
        ) as file:
            data_file = json.load(file)


    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Ошибка при загрузке файла с транзакциями")
        return []

    if not isinstance(data_file, list):
        logger.warning("Данные в файле имеют неверный формат")
        return []

    logger.info("Транзакции успешно загружены")
    return data_file


def convert_to_rub(new_transaction: dict) -> float:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции
    в рублях. Если транзакция была в USD или EUR, отправляем запрос
    к внешнему API для получения текущего курса валют и конвертации в рубли.
    """
    logger.info("Начало конвертации транзакции в рубли")

    amount = float(new_transaction['operationAmount']['amount'])
    currency = new_transaction['operationAmount']['currency']['code']

    if currency == "RUB":
        logger.info("Конвертация не требуется, валюта RUB")
        return amount
    if currency in ("USD", "EUR"):
        logger.info("Запрос курса валюты через API")

        if API_KEY is None:
            raise ValueError("EXCHANGE_API_KEY не найден")

        url = "https://api.apilayer.com/exchangerates_data/latest"

        headers: dict[str, str] = {
            "apikey": API_KEY
        }

        params = {
            "base": currency,
            "symbols": "RUB"
        }

        response = requests.get(url, headers=headers, params=params)
        data_response = response.json()
        rate = float(data_response['rates']['RUB'])

        logger.info("Курс валюты успешно получен")

        amount_rub = amount * rate

        logger.info("Конвертация в рубли успешно выполнена")
        return amount_rub

    raise ValueError(f"Неподдерживаемая валюта: {currency}")

