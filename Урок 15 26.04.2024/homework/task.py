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


def create_file_obj(user_path):
    for dir_path, dir_name, file_name in os.walk(user_path):
        if len(dir_name) > 0:
            print(dir_name)
            for dir_el in dir_name:
                print(dir_el)
        # print(f'{dir_path=}\n{dir_name=}\n{file_name=}\n')

create_file_obj('D:\GB\Python погружение\Python_advanced_cours\Урок 14 21.04.2024')