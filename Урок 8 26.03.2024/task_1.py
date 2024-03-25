import shutil
import json

shutil.copy('D:\\GB\\Python погружение\\Python_advanced_cours\\Урок 7 22.03.2024\\result.txt',
            'D:\\GB\\Python погружение\\Python_advanced_cours\\Урок 8 26.03.2024')


def get_dict(file):
    my_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        while res := f.readline():
            key, value = res.split(' ')
            my_dict[key.capitalize()] = value
    return my_dict


def create_json(file, new_file):
    temp_dict = get_dict(file)
    with open(new_file, 'w', encoding='utf-8') as fj:
        json.dump(temp_dict, fj, ensure_ascii=False)


create_json('result.txt', 'result.json')
