# src/currency_quote/application/ports/outbound/currency_repository.py
from abc import ABC, abstractmethod


class CurrencyRepository(ABC):
    @abstractmethod
    def get_currency_quote(self, currency_code: list):
        pass
