# src/currency_quote/application/ports/outbound/currency_validator_port.py
from abc import ABC, abstractmethod


class CurrencyAPI(ABC):
    @abstractmethod
    def get_last_quote(self, currency_codes) -> dict:
        pass

    @abstractmethod
    def get_history_quote(self, currency_codes) -> dict:
        pass
