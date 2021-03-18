# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос
# к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только
# методы класса str, решить поставленную задачу? Функция должна возвращать результат числового
# типа, например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
#
# *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая
# передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

from requests import get, utils
import datetime


def currency_rates(_currency):
    print()
    if content.find(_currency) == -1:
        return print('Запрашиваемая валюта ' + _currency + ' не найдена.')
    else:
        d1 = content.find('Date')               # поиск даты в данных полученных с сайта
        d2 = content[int(d1) + 6: 70]           # и преобразование её изтипа строки к типу дата
        d3 = d2.split('.')
        yesterday = datetime.date(int(d3[2]), int(d3[1]), int(d3[0]))
        print('На', yesterday, type(yesterday))
        s1 = content.find(_currency)            # поиск введённой валюты и так как формат данных не
        s2 = content[s1:]                       # изменяемый то просто будем отсекать все лишнее
        s3 = s2.find("</Value>")                # что б остался только сам курс валюты
        s4 = s2[:s3]
        s5 = s4.split('<Value>')[1]
        course = float(s5.replace(',', '.'))
        print('Курс', _currency, course, type(course))
        return


def in_put():
    _currency = input('Введите валюту, курс которой хотите узнать (пример: USD, EUR, RON, KZT, BYN)'
                      ' Для завершения введите "exit":')
    return _currency


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

while True:
    currency = in_put()
    if currency.isdigit():
        while currency.isdigit():
            print('Вы ввели не валюту, а цифровое значение. Попробуйте ещё раз.')
            currency = in_put()
    if currency == 'exit':
        break
    currency = currency.upper()
    currency_rates(currency)
    print()
