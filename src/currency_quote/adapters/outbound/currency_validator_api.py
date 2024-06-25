# src/currency_quote/adapters/outbound/currency_validator_api.py
from api_to_dataframe import ClientBuilder, RetryStrategies
from currency_quote.config.endpoints import API


class CurrencyValidator: ##TODO: Precisa depender da Porta de saida
    @staticmethod
    def validate_currency_code(currency_list: list) -> list:
        client = ClientBuilder(
            endpoint=API.ENDPOINT_AVALIABLE_PARITIES,
            retry_strategy=RetryStrategies.LinearRetryStrategy
        )

        valid_list = client.get_api_data()

        validated_list = []

        for currency_code in currency_list:
            if currency_code in valid_list:
                validated_list.append(currency_code)

        return validated_list
