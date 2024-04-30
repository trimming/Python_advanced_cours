# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import logging
from collections import namedtuple
import os

UserFile = namedtuple('UserFile', ['file_name', 'ext', 'parent_dir'])
def create_file_obj(user_path):
    for dir_path, dir_name, file_name in os.walk(user_path):
        if len(dir_name) > 0:
            # print(dir_name)
            for dir_el in dir_name:
                # print(dir_el, 'dir', dir_path.split('\\')[-1])
                u_d = UserFile(dir_el, 'dir', dir_path.split('\\')[-1])
                print(u_d)
        if len(file_name) > 0:
            for file_name_el in file_name:
                # print(file_name_el, file_name_el.split('.')[-1], dir_path.split('\\')[-1])
                u_f = UserFile(file_name_el, file_name_el.split('.')[-1], dir_path.split('\\')[-1])
                print(u_f)
        # print(f'{dir_path=}\n{dir_name=}\n{file_name=}\n')


create_file_obj('D:\GB\Python погружение\Python_advanced_cours\Урок 14 21.04.2024')
