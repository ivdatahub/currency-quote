# src/currency_quote/domain/services/get_currency_quote.py
from currency_quote.application.ports.inbound.get_currency_quote_use_case import GetCurrencyQuoteUseCase
from currency_quote.application.ports.outbound.currency_repository import CurrencyRepository
from currency_quote.domain.entities.currency import Currency
from currency_quote.domain.services.validate_currency import ValidateCurrency


class GetCurrencyQuote(GetCurrencyQuoteUseCase):
    def __init__(self, currency_repository: CurrencyRepository, validate_currency_service: ValidateCurrency):
        self.currency_repository = currency_repository
        self.validate_currency_service = validate_currency_service

    def execute(self, currency_code: str) -> Currency:
        if not self.validate_currency_service.execute(currency_code):
            raise ValueError(f"Código de moeda {currency_code} é inválido.")

        currency = self.currency_repository.get_currency_quote(currency_code)
        if not currency:
            raise ValueError(f"Cotação para a moeda {currency_code} não encontrada.")
        return currency
