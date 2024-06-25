from abc import ABC, abstractmethod
from currency_quote.domain.entities.currency import Currency


class GetCurrencyQuoteUseCase(ABC):
    @abstractmethod
    def execute(self, currency_code: list) -> Currency:
        pass
