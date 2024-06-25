# src/currency_quote/application/services/currency_validator_service.py
from currency_quote.application.ports.outbound.currency_validator_repository import CurrencyValidatorPort
from currency_quote.adapters.outbound.currency_validator_api import CurrencyValidator


class CurrencyValidatorService(CurrencyValidatorPort):
    def __init__(self):
        self.currency_validator = CurrencyValidator()

    def validate_currency_code(self, currency_list: list) -> list:
        validated_list = self.currency_validator.validate_currency_code(currency_list)

        if len(validated_list) == 0:
            raise ValueError(f"All params: {currency_list} are invalid.")

        if len(validated_list) < len(currency_list):
            print(f"Invalid currency params: {set(currency_list) - set(validated_list)}")

        return validated_list
