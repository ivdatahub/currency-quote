from dataclasses import dataclass
from datetime import datetime


class CurrencyQuote:
    def __init__(self, currency_list: list):
        self.currency_list = currency_list

    def get_currency_list(self) -> list:
        if len(self.currency_list) == 0:
            raise ValueError("Currency list is empty")

        return self.currency_list


@dataclass
class Currency:  # pylint: disable=too-many-instance-attributes
    currency_pair: str
    currency_pair_name: str
    base_currency_code: str
    quote_currency_code: str
    quote_timestamp: int
    bid_price: float
    ask_price: float
    quote_extracted_at: int = int(datetime.now().timestamp())
