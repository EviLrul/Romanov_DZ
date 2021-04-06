# Написать скрипт, создающий стартер (заготовку) для проекта со
# следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os


def cr_folders(fol1, fol2):
    temp = os.path.join(fol1, fol2)
    if not os.path.isdir(temp):
        os.makedirs(temp)
    return temp


folders = ['my_project', 'settings', 'adminapp', 'authapp', 'mainapp']
i = 1
while i < len(folders):
    print(cr_folders(folders[0], folders[i]))
    i += 1
