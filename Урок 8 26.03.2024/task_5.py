##Задание №5
##Напишите функцию, которая ищет json файлы в указанной
##директории и сохраняет их содержимое в виде
##одноимённых pickle файлов.


import os
import json
import pickle

def serialize_json(directory):
    if not os.path.exists(directory):
        print('Директория не найдена')
        return

    files = [file for file in os.listdir(directory) if file.endswith('.json')]
    for file_name in files:
        json_path = os.path.join(directory, file_name)
        pickle_path = os.path.join(directory, file_name.split('.')[0] + '.pikle')
        with open(json_path, 'r', encoding='utf-8') as json_file, \
             open(pickle_path, 'wb') as pickle_file:
            data = json.load(json_file)
            pickle.dump(data, pickle_file)

serialize_json('.')
