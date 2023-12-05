import re
import requests
import json


URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'


def load_exchange():
    return json.loads(requests.get(URL).text)


def get_exchange(currency_key):
    for exchange in load_exchange():
        if currency_key == exchange['ccy']:
            return exchange
    return False


def get_exchanges(currency_pattern):
    result = []
    currency_pattern = re.escape(currency_pattern) + '.*'
    for exc in load_exchange():
        if re.match(currency_pattern, exc['ccy'], re.IGNORECASE) is not None:
            result.append(exc)
    return result