from src.utils import convert_to_rub, load_transactions
from unittest.mock import Mock, patch


def test_convert_to_rub():
    transaction = {
        'operationAmount': {'amount': '100', 'currency': {'code': 'RUB'}}
    }

    result = convert_to_rub(transaction)

    assert result == 100


@patch('src.utils.requests.get')
def test_convert_from_usd_to_rub(get_mock):
    transaction = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "USD"
            }
        }
    }
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 80}}
    get_mock.return_value = mock_response
    result = convert_to_rub(transaction)
    assert result == 8000


@patch('src.utils.requests.get')
def test_convert_from_eur_to_rub(get_mock):
    transaction = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "EUR"
            }
        }
    }
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 95}}
    get_mock.return_value = mock_response
    result = convert_to_rub(transaction)
    assert result == 9500


def test_load_transactions():
    result = load_transactions('operations.json')
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], dict)


def test_load_transactions_file_not_found():
    result = load_transactions('NotFound')
    assert result == []


def test_load_transactions_broken_json():
    result = load_transactions('broken.json')
    assert result == []


def test_load_transactions_not_list():
    result = load_transactions('not_list.json')
    assert result == []
