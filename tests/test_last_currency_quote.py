import pytest
from currency_quote import CurrencyQuote


def test_one_valid_param():
    client = CurrencyQuote(['USD-BRL'])

    data = client.get_last_quote()

    assert len(data) == 1
    assert isinstance(data, dict)


def test_two_valid_params():
    client = CurrencyQuote(['USD-BRL', "EUR-BRL"])

    data = client.get_last_quote()

    assert len(data) == 2
    assert isinstance(data, dict)


def test_one_invalid_param():
    client = CurrencyQuote(['USD-BRL', "param1"])

    data = client.get_last_quote()

    assert isinstance(data, dict)
    assert len(data) == 1


def test_all_invalid_params():
    client = CurrencyQuote(['param2', "param1"])

    with pytest.raises(ValueError):
        client.get_last_quote()
