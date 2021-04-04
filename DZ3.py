# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об
# их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них
# словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта
# с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи
import json

new_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f1:
    f2 = open('hobby.csv', 'r', encoding='utf-8')
    for content1 in f1:
        content2 = f2.readline()
        if content2 == '':
            content1 = content1.replace('\n', '').replace('\r', ' ')
            content2 = 'None'
        else:
            content1 = content1.replace('\n', '').replace('\r', ' ')
            content2 = content2.replace('\n', '').replace('\r', ' ')
        new_dict[content1] = content2
f2.close()
with open('user_hobby.csv', 'w', encoding='utf-8') as f:
    f.write(json.dumps(new_dict))

# with open('user_hobby.csv', 'r', encoding='utf-8') as f:
#     cont = json.load(f)
#     print(cont, type(cont))
