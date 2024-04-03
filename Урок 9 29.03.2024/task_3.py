##Задание №3
##Напишите декоратор, который сохраняет в json файл
##параметры декорируемой функции и результат, который она
##возвращает. При повторном вызове файл должен
##расширяться, а не перезаписываться.
##Каждый ключевой параметр сохраните как отдельный ключ
##json словаря.
##Для декорирования напишите функцию, которая может
##принимать как позиционные, так и ключевые аргументы.
##Имя файла должно совпадать с именем декорируемой
##функции.
import json
import os.path
from functools import wraps


def writer_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                data_json = json.load(file)
                current_id = int(max(data_json, key=lambda x: int(x))) + 1
        else:
            data_json = {}
            current_id = 1
        res = func(*args, **kwargs)
        data_json[current_id] = {'func_name': func.__name__, 'result': res, 'args': args, 'kwargs': {}}
        for key, value in kwargs.items():
            data_json[current_id]['kwargs'][key] = value
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    return wrapper


@writer_json
def summa_args(*args, **kwargs):
    return sum(args)


summa_args(1, 3, 2, 2, 5, 10, 8, 9, k='6', l='8')
