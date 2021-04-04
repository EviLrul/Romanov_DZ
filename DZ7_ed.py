# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться
# целиком — обязательное требование. Предусмотреть ситуацию, когда пользователь вводит
# номер записи, которой не существует.
import sys

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    line_edit = int(sys.argv[1]) * 12
    check_line = f.seek(0, 2)
    if check_line < line_edit:
        print('Увы, такой записи нет')
    else:
        f.seek(line_edit - 12)
        line_len = 10 - len(sys.argv[2])
        f.write(sys.argv[2] + '-' * line_len + '\n')
