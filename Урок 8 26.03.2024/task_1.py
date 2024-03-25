import shutil
import json

shutil.copy('D:\\GB\\Python погружение\\Python_advanced_cours\\Урок 7 22.03.2024\\result.txt',
            'D:\\GB\\Python погружение\\Python_advanced_cours\\Урок 8 26.03.2024')


def create_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        while res := f.readline():
            print(res)


create_json('result.txt')
