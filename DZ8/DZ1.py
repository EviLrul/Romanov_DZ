# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

import re
list_data = ('sdf_45dsf@yandex56_w.com', 'sdf_45d@yandex.ru', 'nagibator3000@ya.com', 'Es5dsf@g_mail.com',
             'nagibator30@mail.com', 'nagir00ya.com')

itog_dict = {}


def email_parse(email_address):
    reg = re.split(r'@', email_address)
    if len(reg) < 2:
        raise ValueError('Почта ' + '"' + email_address + '"' + ' не валидна... нет "@"')
    reg1 = re.split(r'\.', reg[1])
    if len(reg1) < 2:
        raise ValueError('Почта ' + '"' + email_address + '"' + ' не валидна... нет "." в домене')
    return reg


for _data in list_data:
    data = email_parse(_data)
    print(data)
    itog_dict[data[0]] = data[1]
print(itog_dict)
