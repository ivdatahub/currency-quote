# src/currency_quote/application/ports/outbound/currency_validator_port.py
from abc import ABC, abstractmethod


class CurrencyValidatorPort(ABC):
    @abstractmethod
    def validate_currency_code(self, currency_list: list) -> list:
        pass
