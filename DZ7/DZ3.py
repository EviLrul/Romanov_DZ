# Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт,
# который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
import os
import shutil

path_folders = 'my_project'
list_folders = os.listdir(path_folders)
for name_folders in list_folders:
    temp_data1 = os.listdir(os.path.join(path_folders, name_folders))
    for i in range(len(temp_data1)):
        if temp_data1[i] == 'templates':
            temp_path = os.path.join(path_folders, name_folders, 'templates', name_folders)
            temp_path1 = os.path.join(path_folders, 'templates', name_folders)
            if not os.path.isdir(temp_path1):
                os.makedirs(temp_path1)
            temp_files = os.listdir(temp_path)
            for j in range(len(temp_files)):
                shutil.copy2(os.path.join(temp_path, temp_files[j]), os.path.join(temp_path1, temp_files[j]))
