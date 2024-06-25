# src/currency_quote/application/use_cases/validate_currency.py
from currency_quote.domain.services.validate_currency import CurrencyValidatorService
from currency_quote.domain.entities.currency import Currency


class ValidateCurrencyUseCase:
    def __init__(self, currency_validator_service: CurrencyValidatorService):
        self.currency_validator_service = currency_validator_service

    def execute(self, currency_list: list) -> list:
        return self.currency_validator_service.validate_currency_code(currency_list)
