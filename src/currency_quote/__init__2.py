# currency.py

class Currency:
    def __init__(self, currency_list: list):
        self.currency_list = currency_list

    def get_currency_list(self) -> list:
        return self.currency_list

    def add_currency(self, currency_code: str):
        if currency_code not in self.currency_list:
            self.currency_list.append(currency_code)
        # Poderia adicionar lógica de tratamento caso a moeda já exista, caso haja interesse.

### Integração com Serviços (Services)

Nos seus serviços, como `CurrencyValidatorService`, você pode usar objetos `Currency` para manipular e processar a lista de moedas:

```python
# currency_validator_service.py

from currency_quote.domain.entities.currency import Currency

class CurrencyValidatorService:
    def __init__(self, currency: Currency):
        self.currency = currency

    def validate_currency_code(self, currency_list: list) -> list:
        valid_currencies = []
        for currency_code in currency_list:
            if currency_code in self.currency.get_currency_list():
                valid_currencies.append(currency_code)
            else:
                print(f"Currency code: {currency_code} is not valid")

        if not valid_currencies:
            raise ValueError("No valid currency codes were provided")

        return valid_currencies

    def add_currency(self, currency_code: str):
        self.currency.add_currency(currency_code)

### Caso de Uso (Use Case)

No seu caso de uso `ValidateCurrencyUseCase`, você pode utilizar o serviço `CurrencyValidatorService` da seguinte maneira:

```python
# validate_currency.py

from currency_quote.application.services.currency_validator_service import CurrencyValidatorService

class ValidateCurrencyUseCase:
    def __init__(self, currency_validator_service: CurrencyValidatorService):
        self.currency_validator_service = currency_validator_service

    def execute(self, currency_list: list) -> list:
        return self.currency_validator_service.validate_currency_code(currency_list)
