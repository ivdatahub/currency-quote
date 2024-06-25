from .adapters.outbound.currency_api import CurrencyAPI
from .adapters.inbound.controller import CurrencyController
from .domain.services.get_currency_quote import GetCurrencyQuote
from .domain.services.validate_currency import ValidateCurrency



class CurrencyQuote:
    def __init__(self):
        currency_api = CurrencyAPI()
        validate_currency_service = ValidateCurrency(currency_api)
        get_currency_quote_service = GetCurrencyQuote(currency_api, validate_currency_service)
        self.controller = CurrencyController(get_currency_quote_service)

    def get_quote(self, currency_code: str):
        return self.controller.get_quote(currency_code)
