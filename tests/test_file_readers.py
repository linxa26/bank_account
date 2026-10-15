from src.file_readers import read_csv_transactions
from src.file_readers import read_excel_transactions
import pandas as pd
from unittest.mock import mock_open, patch


def test_read_csv_transactions(tmp_path):
    file_path = tmp_path / 'test.csv'
    file_path.write_text(
        'id;state;amount\n'
        '1;EXECUTED;1500\n'
        '2;CANCELED;3000\n',
        encoding='utf-8'
    )
    result = read_csv_transactions(file_path)

    assert result == [
        {"id": "1", "state": "EXECUTED", "amount": "1500"},
        {"id": "2", "state": "CANCELED", "amount": "3000"}
    ]


def test_read_excel_transactions(tmp_path):
    file_path = tmp_path / "test.xlsx"

    data = {
        "id": [1, 2],
        "state": ["EXECUTED", "CANCELED"],
        "amount": [1500, 3000]
    }

    df = pd.DataFrame(data)

    df.to_excel(file_path, index=False)
    result = read_excel_transactions(file_path)

    assert result == [
        {"id": 1, "state": "EXECUTED", "amount": 1500},
        {"id": 2, "state": "CANCELED", "amount": 3000}
    ]


def test_read_csv_with_mock():
    csv_data = "id;state;amount\n1;EXECUTED;1500\n"

    with patch("builtins.open", mock_open(read_data=csv_data)):
        result = read_csv_transactions("fake.csv")

    assert result == [
        {"id": "1", "state": "EXECUTED", "amount": "1500"}
    ]
