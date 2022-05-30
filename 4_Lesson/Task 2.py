import requests
import re
import datetime


def currency_rates(url, currency):
    #currency = input('Insert your currency: ')
    currency = currency.upper()
    URL = requests.get(url).text
    URL = re.split('[<|>]', URL)
    i = 0

    while i < len(URL):
        if URL[i] == currency:
            return f'{float(URL[i + 12].replace(",", "."))}'
        else:
            i += 1

print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'usD'))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'usd2'))

