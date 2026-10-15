import csv

import pandas as pd


def read_csv_transactions(file_path):
    """
    Считывает финансовые операции из CSV-файла.

    Принимает путь к CSV-файлу, читает его содержимое
    и возвращает список словарей с транзакциями.
    """
    with open(file_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        transactions = list(reader)
        return transactions


def read_excel_transactions(file_path):
    """
    Считывает финансовые операции из Excel-файла.

    Принимает путь к XLSX-файлу, преобразует данные
    в список словарей и возвращает его.
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict(orient="records")
    return transactions
