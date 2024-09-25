import pytest
from currency_quote.domain.entities.currency import CurrencyObject


def test_currency_object():
    client = CurrencyObject(currency_list=["USD-BRL"])
    assert client.get_currency_list() == ["USD-BRL"]


def test_currency_object_with_str():
    client = CurrencyObject(currency_list="USD-BRL")
    assert client.get_currency_list() == ["USD-BRL"]


def test_currency_object_with_empty_list():
    with pytest.raises(ValueError):
        CurrencyObject(currency_list=[])


def test_currency_object_with_empty_str():
    with pytest.raises(ValueError):
        CurrencyObject(currency_list="")


def test_currency_object_with_invalid_currency_code():
    with pytest.raises(ValueError):
        CurrencyObject(currency_list=["USD-BR"])


def test_currency_object_with_invalid_types():
    with pytest.raises(TypeError):
        CurrencyObject(currency_list=12312421312)


def test_currency_object_with_formats():
    currency_list = ["param1", "param2"]
    with pytest.raises(ValueError):
        CurrencyObject(currency_list)
