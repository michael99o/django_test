import requests
import json
from config import keys

class ApiException(Exception):
    pass

class CurrencyConvertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ApiException(f'Невозможно перевести одинаковые валюты - {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту - {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту - {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Не удалось обработать количество - {amount}')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/12d0ba2113f07712b597be3e/pair/{quote_ticker}/{base_ticker}/{amount}')
        total_base = json.loads(r.content)['conversion_result']

        return total_base
