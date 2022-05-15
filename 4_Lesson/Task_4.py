import requests
import re
import datetime


def currency_rates(url='http://www.cbr.ru/scripts/XML_daily.asp', currency='USD'):
    currency = currency.upper()
    URL = requests.get(url).text
    URL = re.split('[<|>]', URL)
    i = 0

    while i < len(URL):
        if URL[i] == currency:
            return f'{float(URL[i + 12].replace(",", "."))}'
        else:
            i += 1



def currency_rates_advanced(url='http://www.cbr.ru/scripts/XML_daily.asp', currency='EUR'):
    currency = currency.upper()
    URL = requests.get(url).text
    date1 = re.findall(r'\d{2}\.\d{2}\.\d{4}', URL)
    d, m, y = ''.join(date1).split('.')
    d, m, y = int(d), int(m), int(y)
    final_date = datetime.date(y, m, d)
    URL = re.split('[<|>]', URL)
    i = 0

    while i < len(URL):
        if URL[i] == currency:
            return f'{final_date}, {float(URL[i + 12].replace(",", "."))}'
        else:
            i += 1



if __name__ == "__main__":
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'amD'))
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'usd2'))

    print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', 'amD'))
    print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', 'amDw'))

