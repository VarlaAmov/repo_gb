import requests
import re
import datetime


def currency_rates_advanced(url, currency):
    # currency = input('Insert your currency: ')
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

print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', 'EuR'))
print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', 'euRw'))
