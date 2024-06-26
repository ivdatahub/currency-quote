# src/currency_quote/application/use_cases/validate_currency.py
from currency_quote.domain.services.validate_currency import CurrencyValidatorService
from currency_quote.adapters.outbound.currency_validator_api import CurrencyValidator
from currency_quote.domain.entities.currency import Currency


class ValidateCurrencyUseCase:
    @staticmethod
    def execute(currency_list: list) -> list:
        currency_object = Currency(currency_list)
        validator_service = CurrencyValidatorService(
            currency=currency_object,
            currency_validator=CurrencyValidator
        )
        return validator_service.validate_currency_code(currency_list)
