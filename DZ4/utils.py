import datetime


def currency_rates(_currency, _content):
    print()
    if _content.find(_currency) == -1:
        return print('Запрашиваемая валюта ' + _currency + ' не найдена.')
    else:
        d1 = _content.find('Date')               # поиск даты в данных полученных с сайта
        d2 = _content[int(d1) + 6: 70]           # и преобразование её изтипа строки к типу дата
        d3 = d2.split('.')
        yesterday = datetime.date(int(d3[2]), int(d3[1]), int(d3[0]))
        print('На', yesterday, type(yesterday))
        s1 = _content.find(_currency)            # поиск введённой валюты и так как формат данных не
        s2 = _content[s1:]                       # изменяемый то просто будем отсекать все лишнее
        s3 = s2.find("</Value>")                 # что б остался только сам курс валюты
        s4 = s2[:s3]
        s5 = s4.split('<Value>')[1]
        course = float(s5.replace(',', '.'))
        print('Курс', _currency, course, type(course))
        return


def in_put():
    _currency = input('Введите валюту, курс которой хотите узнать (пример: USD, EUR, RON, KZT, BYN)'
                      ' Для завершения введите "exit":')
    return _currency
