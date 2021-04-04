# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает
# объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто
# задел на будущее проекта). Только теперь не нужно создавать словарь с данными.
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
# Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

new_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f1:
    f2 = open('hobby.csv', 'r', encoding='utf-8')
    f3 = open('users_hobby.txt', 'w', encoding='utf-8')
    line_f1 = f1.readline()
    while line_f1:
        line_f1 = line_f1.replace('\n', '').replace('\r', ' ')
        line_f2 = f2.readline()
        line_f2 = line_f2.replace('\n', '').replace('\r', ' ')
        if line_f2 == '':
            f3.write(line_f1 + ': None\n')
        else:
            f3.write(line_f1 + ': ' + line_f2 + '\n')
        line_f1 = f1.readline()
f2.close()
f3.close()
