import utils
from sys import argv

print('Parsing URL: "http://www.cbr.ru/scripts/XML_daily.asp"')
URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

print('\nCurrency without datetime:')
print(utils.currency_rates(URL, 'uSd'))
#print(utils.currency_rates(URL, argv[1])) -- 5 задание не доделал

print('\nCurrency with datetime:')
print(utils.currency_rates_advanced(URL, 'UaH'))
#print(utils.currency_rates_advanced(URL, argv[1])) -- 5 задание не доделал

