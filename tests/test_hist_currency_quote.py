import pytest
import datetime
from currency_quote import CurrencyQuote



def test_one_valid_param():
    client = CurrencyQuote(['USD-BRL'])

    data = client.get_history_quote(reference_date=20240526)

    assert len(data) == 1
    assert isinstance(data, list)


def test_two_valid_params():
    client = CurrencyQuote(['USD-BRL', "EUR-BRL"])

    data = client.get_history_quote(reference_date=20240526)

    assert len(data) == 2
    assert isinstance(data, list)


def test_one_invalid_param():
    client = CurrencyQuote(['USD-BRL', "param1"])

    data = client.get_history_quote(reference_date=20240526)

    assert isinstance(data, list)
    assert len(data) == 1


def test_all_invalid_params():
    client = CurrencyQuote(['param2', "param1"])

    with pytest.raises(ValueError):
        client.get_history_quote(reference_date=20240526)


def test_invalid_date():
    client = CurrencyQuote(['USD-BRL'])

    invalid_date = int(datetime.datetime.now().strftime("%Y%m%d")) + 1

    with pytest.raises(ValueError):
        client.get_history_quote(reference_date=invalid_date)
        
        
def test_indisponible_data():
    client = CurrencyQuote(['USD-BRL'])

    invalid_date = 20160110

    with pytest.raises(ValueError):
        client.get_history_quote(reference_date=invalid_date)
