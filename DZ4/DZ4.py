# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

from requests import get, utils
from utils import in_put, currency_rates

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
# print(content)

while True:
    currency = in_put()
    if currency.isdigit():
        while currency.isdigit():
            print('Вы ввели не валюту, а цифровое значение. Попробуйте ещё раз.')
            currency = in_put()
    if currency == 'exit':
        break
    currency = currency.upper()
    currency_rates(currency, content)
    print()
