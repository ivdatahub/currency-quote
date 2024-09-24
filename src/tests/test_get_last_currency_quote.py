from currency_quote.application.use_cases.get_last_currency_quote import (
    GetLastCurrencyQuoteUseCase,
)
from currency_quote.domain.entities.currency import CurrencyQuote, CurrencyObject


def test_valid_currency():
    currency_list = ["USD-BRL", "EUR-BRL"]
    currency_quote = CurrencyObject(currency_list)
    result = GetLastCurrencyQuoteUseCase.execute(currency_quote)
    for item in result:
        assert isinstance(item, CurrencyQuote)

    assert len(result) == 2


def test_partial_valid_currency():
    currency_list = ["USD-BRL", "EUR-BRL", "AAA-BBB"]
    currency_quote = CurrencyObject(currency_list)
    result = GetLastCurrencyQuoteUseCase.execute(currency_quote)
    for item in result:
        assert isinstance(item, CurrencyQuote)

    assert len(result) == 2
