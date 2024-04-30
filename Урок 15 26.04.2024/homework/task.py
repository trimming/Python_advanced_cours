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
from exception import *
import logging
from collections import namedtuple
import os
import argparse

UserFile = namedtuple('UserFile', ['file_name', 'ext', 'parent_dir'])

FORMAT = '{levelname:10} {asctime:20} {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='log.log', filemode='a+', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def create_file_obj(user_path: str):
    if os.path.isdir(user_path):
        for dir_path, dir_name, file_name in os.walk(user_path):
            if len(dir_name) > 0:
                for dir_el in dir_name:
                    u_d = UserFile(dir_el, 'dir', dir_path.split('\\')[-1])
                    data = f'Создан объект с именем - {u_d.file_name}, флагом:{u_d.ext} каталога "{u_d.parent_dir}"'
                    logger.info(data)
            if len(file_name) > 0:
                for file_name_el in file_name:
                    u_f = UserFile(file_name_el, file_name_el.split('.')[-1], dir_path.split('\\')[-1])
                    data = f'Создан объект с именем - {u_f.file_name}, расширением:{u_f.ext} каталога "{u_f.parent_dir}"'
                    logger.info(data)
    else:
        raise MyDirError(user_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('param', metavar='path', type=str, nargs='*')
    args = parser.parse_args()
    create_file_obj(*args.param)
