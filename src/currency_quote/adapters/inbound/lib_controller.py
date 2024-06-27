from abc import ABC
from currency_quote.application.ports.inbound.controller import IController
from currency_quote.application.use_cases.get_last_currency_quote import GetLastCurrencyQuoteUseCase
from currency_quote.application.use_cases.get_history_currency_quote import GetHistCurrencyQuoteUseCase


class LibController(IController, ABC):

    def __init__(self):
        pass

    def get_last_quote(self, currency_list: list) -> dict:
        return GetLastCurrencyQuoteUseCase.execute(currency_list=currency_list)

    def get_historical_quotes(self, currency_list: list, reference_date: int) -> dict:
        return GetHistCurrencyQuoteUseCase.execute(currency_list=currency_list, reference_date=reference_date)
