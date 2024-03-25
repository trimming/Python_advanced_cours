# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.
import random as rd

MIN_LEN = 4
MAX_LEN = 7


def gen_name(num_name: int, file_name: str):
    with open(file_name, 'w+', encoding='utf-8') as f:
        all_letter = 'абвгдеёжзийклмнопрстуфхцчшщэюя'
        con_letter = 'бвгджзйклмнпрстфхцчшщъь'
        vow_letter = 'аеёиоуэюя'
        for _ in range(num_name):
            name = ''
            name_len = rd.randint(MIN_LEN, MAX_LEN)
            for _ in range(name_len):
                if len(name) > 1:
                    if name[-1] in vow_letter:
                        name += rd.choice(con_letter)
                    else:
                        name += rd.choice(vow_letter)
                else:
                    name += rd.choice(all_letter)
            f.write(f'{name.capitalize()}\n')


gen_name(7, 'names.txt')
