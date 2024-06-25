from .config.endpoints import API
from api_to_dataframe import ClientBuilder, RetryStrategies
import datetime


class CurrencyQuote:
    def __init__(self, currency_list: list):
        self.currency_code = currency_list

    @staticmethod
    def _get_history_quote(*args, reference_date: int):

        result = []

        for currency_code in args:
            url = \
                (f"{API.ENDPOINT_HISTORY_COTATION}"
                 f"{currency_code}"
                 f"/?start_date={reference_date}&end_date={reference_date}")

            client = ClientBuilder(
                endpoint=url,
                retry_strategy=RetryStrategies.LinearRetryStrategy
            )

            response = client.get_api_data()

            result.append(response[0])

        return result

    def get_history_quote(self, reference_date: int):
        today = int(datetime.datetime.now().strftime("%Y%m%d"))
        if reference_date > today:
            raise ValueError(
                f"Reference date: {reference_date} is not valid. "
                f"Make sure you give a correct reference date, e.g.: {today}"
            )

        if reference_date < 20160111:
            raise ValueError(
                f"The data is only available from 2016-01-11."
            )

        hist_quote = self._get_history_quote(*self._validate_currency_code(), reference_date=reference_date)

        return hist_quote
