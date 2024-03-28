##Задание №5
##Напишите функцию, которая ищет json файлы в указанной
##директории и сохраняет их содержимое в виде
##одноимённых pickle файлов.


import os
import json
import pikle

def serialize_json(directory):
    if not os.path.exists(directory):
        print('Директория не найдена')
        return

    files = [file for file in os.listdir(directory) if file.endswith('.json')]
    for file in files:
        json_path = os.path.join(directory, file_name)
        pickle_path = os.path.
