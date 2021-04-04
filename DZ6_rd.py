# Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных
# и для вывода на экран записанных данных. При записи передавать из командной
# строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# - просто запуск скрипта — выводить все записи;
# - запуск скрипта с одним параметром-числом — выводить все записи с номера,
# равного этому числу, до конца;
# - запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно.

# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
# Примеры запуска скриптов:

# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

import sys

start_line = ''
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        print(f.read().replace('-', ''))
    elif len(sys.argv) == 2:
        start_line_flag = int(sys.argv[1])
        start_line = f.readline()
        start_line = start_line.replace('\n', '').replace('\r', ' ').replace('-', '')
        flag_start = 1
        while start_line:
            start_line = f.readline()
            start_line = start_line.replace('\n', '').replace('\r', ' ').replace('-', '')
            flag_start += 1
            if flag_start == start_line_flag:
                print(start_line)
                flag_start -= 1
    elif len(sys.argv) == 3:
        start_line_flag = int(sys.argv[1])
        end_line_flag = int(sys.argv[2])
        counter_line = end_line_flag - start_line_flag
        start_line = f.readline()
        start_line = start_line.replace('\n', '').replace('\r', ' ').replace('-', '')
        flag_start = 1
        while start_line:
            start_line = f.readline()
            start_line = start_line.replace('\n', '').replace('\r', ' ').replace('-', '')
            flag_start += 1
            if flag_start == start_line_flag:
                if counter_line == -1:
                    break
                print(start_line)
                flag_start -= 1
                counter_line -= 1
