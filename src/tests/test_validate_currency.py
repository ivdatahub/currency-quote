from currency_quote.application.use_cases.validate_currency import (
    ValidateCurrencyUseCase,
)
from currency_quote.domain.entities.currency import CurrencyObject


def test_valid_currency():
    currency_list = ["USD-BRL", "USD-BRLT"]
    currency_quote = CurrencyObject(currency_list)
    result = ValidateCurrencyUseCase.execute(currency_quote=currency_quote)
    assert result.get_currency_list() == currency_list
    assert isinstance(result, CurrencyObject)


def test_partial_valid_currency():
    currency_list = ["USD-BRL", "USD-BRLT", "AAA-BBB"]
    currency_quote = CurrencyObject(currency_list)
    expected_result = ["USD-BRL", "USD-BRLT"]
    result = ValidateCurrencyUseCase.execute(currency_quote=currency_quote)
    assert result.get_currency_list() == expected_result
    assert isinstance(result, CurrencyObject)
