import pytest
from currency_quote.domain.services.validate_currency import CurrencyValidatorService
from currency_quote.application.use_cases.validate_currency import ValidateCurrencyUseCase


def test_valid_currency():
    validator_service = CurrencyValidatorService()
    currency_list = ["USD-BRL", "USD-BRLT"]
    validate_currency = ValidateCurrencyUseCase(currency_validator_service=validator_service)
    result = validate_currency.execute(currency_list=currency_list)
    assert result == currency_list


def test_partial_valid_currency():
    validator_service = CurrencyValidatorService()
    currency_list = ["USD-BRL", "USD-BRLT", "param1"]
    expected_result = ["USD-BRL", "USD-BRLT"]
    validate_currency = ValidateCurrencyUseCase(currency_validator_service=validator_service)
    result = validate_currency.execute(currency_list=currency_list)
    assert result == expected_result


def test_invalid_currency():
    validator_service = CurrencyValidatorService()
    currency_list = ["param1", "param2"]
    validate_currency = ValidateCurrencyUseCase(currency_validator_service=validator_service)
    with pytest.raises(ValueError):
        validate_currency.execute(currency_list=currency_list)

