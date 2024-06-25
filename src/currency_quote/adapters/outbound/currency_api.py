# src/currency_quote/adapters/outbound/currency_api.py
from api_to_dataframe import ClientBuilder, RetryStrategies
from currency_quote.application.ports.outbound.currency_repository import CurrencyRepository
from currency_quote.config.endpoints import API


class CurrencyAPI(CurrencyRepository):
    def _get_last_quote(*args):
        url = API.ENDPOINT_LAST_COTATION + ','.join(args)
        client = ClientBuilder(
            endpoint=url,
            retry_strategy=RetryStrategies.LinearRetryStrategy
        )

        response = client.get_api_data()

        return response