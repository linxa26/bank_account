from pathlib import Path
import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")


def load_transactions(operation: str) -> list:
    """Функция загружает транзакции из JSON-файла"""
    try:
        with open(
                Path(__file__).parent.parent / "data" / operation,
                encoding="utf-8"
        ) as file:
            data_file = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not isinstance(data_file, list):
        return []

    return data_file


def convert_to_rub(new_transaction: dict) -> float:
    """
       Функция, принимает на вход транзакцию и возвращает сумму транзакции
       в рублях. Если транзакция была в USD или EUR, отправляем запрос
       к внешнему API для получения текущего курса валют и конвертации в рубли.
       """
    amount = float(new_transaction['operationAmount']['amount'])
    currency = new_transaction['operationAmount']['currency']['code']
    if currency == "RUB":
        return amount
    if currency in ("USD", "EUR"):
        url = "https://api.apilayer.com/exchangerates_data/latest"
        headers = {
            "apikey": API_KEY
        }

        params = {
            "base": currency,
            "symbols": "RUB"
        }

        response = requests.get(url, headers=headers, params=params)
        data_response = response.json()
        rate = data_response['rates']['RUB']
        amount_rub = amount * rate
        return amount_rub
