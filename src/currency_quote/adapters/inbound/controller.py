# src/currency_quote/adapters/inbound/controller.py
from currency_quote.application.ports.inbound.get_currency_quote_use_case import GetCurrencyQuoteUseCase


class CurrencyController:
    def __init__(self, get_currency_quote_use_case: GetCurrencyQuoteUseCase):
        self.get_currency_quote_use_case = get_currency_quote_use_case

    def get_quote(self, currency_code: str):
        try:
            currency = self.get_currency_quote_use_case.execute(currency_code)
            return {"code": currency.code, "name": currency.name, "rate": currency.rate}
        except ValueError as e:
            return {"error": str(e)}
