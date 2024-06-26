from api_to_dataframe import ClientBuilder, RetryStrategies
from currency_quote.application.ports.outbound.currency_repository import CurrencyAPI
from currency_quote.config.endpoints import API


class CurrencyAPI(CurrencyAPI):

    def __init__(self, currency_codes):
        self.currency_codes = currency_codes

    def get_last_quote(self):
        url = f"{API.ENDPOINT_LAST_COTATION}/{self.currency_codes}"
        client = ClientBuilder(
            endpoint=url,
            retry_strategy=RetryStrategies.ExponentialRetryStrategy
        )

        response = client.get_api_data()

        return response

    def get_history_quote(self, reference_date: int):
        pass
    