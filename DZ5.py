# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла.
# Проверить работу скрипта.
import sys

new_dict = {}
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
input_file3 = sys.argv[3]
with open(input_file1, 'r', encoding='utf-8') as f1:
    f2 = open(input_file2, 'r', encoding='utf-8')
    f3 = open(input_file3, 'w', encoding='utf-8')
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
