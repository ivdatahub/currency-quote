from .config.endpoints import API
from api_to_dataframe import ClientBuilder, RetryStrategies


class CurrencyQuote:
    def __init__(self, currency_list: list):
        self.currency_code = currency_list

    def _validate_currency_code(self) -> list:
        client = ClientBuilder(
            endpoint=API.ENDPOINT_AVALIABLE_PARITIES,
            retry_strategy=RetryStrategies.LinearRetryStrategy
        )

        valid_list = client.get_api_data()

        validated_list = []

        for currency_code in self.currency_code:
            if currency_code in valid_list:
                validated_list.append(currency_code)
            else:
                print(f"Currency code: {currency_code} is not valid")

            if len(validated_list) == 0:
                raise ValueError("No valid currency code was provided")

        return validated_list

    @staticmethod
    def _get_last_quote(*args):
        url = API.ENDPOINT_LAST_COTATION + ','.join(args)
        client = ClientBuilder(
            endpoint=url,
            retry_strategy=RetryStrategies.LinearRetryStrategy
        )

        response = client.get_api_data()

        return response

    def get_last_quote(self):
        last_quote = self._get_last_quote(*self._validate_currency_code())
        return last_quote

    def get_history_quote(self, reference_date: int):
        """
        Title: get_history_quote
        params: reference_date (int)
        example: 20240526

        returns: the json data with quote of reference_date

        """
        url = \
            (f"{API.ENDPOINT_HISTORY_COTATION}"
             f"{self._validate_currency_code()}"
             f"/?start_date={reference_date}&end_date={reference_date}")

        client = ClientBuilder(
            endpoint=url,
            retry_strategy=RetryStrategies.ExponentialRetryStrategy
        )

        response = client.get_api_data()

        return response
