# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


def create_json(in_file, out_file):
    with open(in_file, 'r', encoding='utf-8') as input_file:
        data = input_file.readlines()
    data = {row.strip().split()[0].capitalize(): float(row.strip().split()[1]) for row in data}
    with open(out_file, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, indent=2, ensure_ascii=False)


create_json('result.txt', 'result.json')
