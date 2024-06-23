from currency_quote import CurrencyQuote

client = CurrencyQuote(["USD-BRL", "USD-BRLT"])

print(client.get_last_quote())
