# *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import sys
from requests import get, utils
from utils import currency_rates

input_argument = sys.argv[1]
input_argument = input_argument.upper()
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

currency_rates(input_argument, content)



