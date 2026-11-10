import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")


def load_transactions(operation: str) -> list:
    """Загружает банковские транзакции из JSON-файла."""
    try:
        with open(
            Path(__file__).parent.parent / "data" / operation,
            encoding="utf-8",
        ) as file:
            data_file = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not isinstance(data_file, list):
        return []

    return data_file


def convert_to_rub(new_transaction: dict) -> float:
    """Конвертирует сумму транзакции из RUB, USD или EUR в рубли."""
    amount = float(new_transaction["operationAmount"]["amount"])
    currency = new_transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        if not API_KEY:
            raise ValueError("Не указан API-ключ EXCHANGE_API_KEY")

        url = "https://api.apilayer.com/exchangerates_data/latest"

        headers = {"apikey": API_KEY}

        params = {
            "base": currency,
            "symbols": "RUB",
        }

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10,
        )
        response.raise_for_status()

        data_response = response.json()
        rate = float(data_response["rates"]["RUB"])

        amount_rub = amount * rate
        return amount_rub

    raise ValueError(f"Неподдерживаемая валюта: {currency}")
