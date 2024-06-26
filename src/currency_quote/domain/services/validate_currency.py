# src/currency_quote/application/services/currency_validator_service.py
from currency_quote.domain.entities.currency import Currency
from currency_quote.application.ports.outbound.currency_validator_repository import CurrencyValidatorPort
from typing import Type


class CurrencyValidatorService:
    def __init__(self, currency: Currency, currency_validator: Type[CurrencyValidatorPort]):
        self.currency_validator = currency_validator
        self.currency_list = currency.get_currency_list()

    def validate_currency_code(self, currency_list: list) -> list:
        validated_list = self.currency_validator.validate_currency_code(currency_list)

        if len(validated_list) == 0:
            raise ValueError(f"All params: {currency_list} are invalid.")

        if len(validated_list) < len(currency_list):
            print(f"Invalid currency params: {set(currency_list) - set(validated_list)}")

        return validated_list
