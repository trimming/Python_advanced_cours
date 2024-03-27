# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os


def input_name(message: str) -> str:
    return input(message)


def input_lvl(message: str, error_message: str, limits: tuple[int, int]) -> str:
    while True:
        level = input(message)
        if level.isdigit() and limits[0] <= int(level) <= limits[1]:
            return level
        print(error_message)


def input_id(message: str, error_message, id_is_exists: str, id_list: list[str]) -> str:
    while True:
        user_id = input(message)
        if user_id.isdigit():
            if user_id not in id_list:
                return user_id
            else:
                print(id_is_exists)
        else:
            print(error_message)


def input_users(file_name: str) -> None:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            users_dict = json.load(file)
    else:
        users_dict = {}
    users_id_list = [u_id for users in users_dict.values() for u_id in users]
    while True:
        user_name = input_name('Введите имя пользователя: ')
        if not user_name:
            break
        user_id = input_id('Введите ID пользователя: ', 'ID должен состоять исключительно из цифр!',
                           'Пользователь с таким ID уже существует!', users_id_list)
        user_level = input_lvl('Введите уровень пользователя от 1 до 7: ', 'Нужно ввести число от 1 до 7', (1, 7))
        # user_levels_list = sorted(users_dict, key=lambda x: int(x))
        # users_dict = {user_lvl: users_dict[user_lvl] for user_lvl in user_levels_list}
        if user_level in users_dict:
            users_dict[user_level][user_id] = user_name
        else:
            users_dict[user_level] = {user_id: user_name}
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(users_dict, file, indent=4, ensure_ascii=False, sort_keys=True)
        users_id_list.append(user_id)


input_users('users_list.json')
