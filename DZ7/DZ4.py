# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
# например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os


def creat_tuple(_key_size_file):
    if _key_size_file not in final_tuple:
        final_tuple[_key_size_file] = 1
    else:
        final_tuple[_key_size_file] += 1
    return final_tuple


final_tuple = {}
tree = os.walk('my_project')
for i in tree:
    paths = i[0]
    files = i[2]
    for j in range(len(files)):
        paths_end = os.path.join(paths, files[j])
        size_file = os.path.getsize(paths_end)
        if 0 <= size_file <= 9:
            key_size_file = 10
            creat_tuple(key_size_file)
        elif 10 <= size_file <= 99:
            key_size_file = 100
            creat_tuple(key_size_file)
        elif 100 <= size_file <= 999:
            key_size_file = 1000
            creat_tuple(key_size_file)
        elif 1000 <= size_file <= 9999:
            key_size_file = 10000
            creat_tuple(key_size_file)
        elif 10000 <= size_file <= 99999:
            key_size_file = 100000
            creat_tuple(key_size_file)
print(final_tuple, type(final_tuple))
