from abc import ABC, abstractmethod


class IController(ABC):

    @abstractmethod
    def get_last_quote(self, currency_list: list) -> dict:
        pass

    @abstractmethod
    def get_history_quote(self, currency_list: list, reference_date: int) -> dict:
        pass
