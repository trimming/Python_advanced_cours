##Задание №6
##Напишите функцию, которая преобразует pickle файл
##хранящий список словарей в табличный csv файл.
##Для тестированию возьмите pickle версию файла из задачи
##4 этого семинара.
##Функция должна извлекать ключи словаря для заголовков
##столбца из переданного файла

import pickle
import csv
import os

def pickle_to_csv(path_pickle: str, headers):
    current_path_pickle = os.path.split(path_pickle)
    path_csv = os.path.join(current_path_pickle[0], current_path_pickle[-1].split('.')[0] + '.csv')
    with open(path_pickle, 'rb') as pickle_file, \
         open(path_csv, 'w', encoding='utf-8', newline='') as csv_file:
        data = pickle.load(pickle_file)
        csv_writer = csv.writer(csv_file)
        for user_lvl, users in data.items():
            for user_id, user_name in users.items():
                csv_writer.writerow([user_name, user_id, user_lvl])

pickle_to_csv('C:\\Users\\User\\Desktop\\IT\\Python погружение\\Python_advanced_cours\\Урок 8 26.03.2024\\users_list.pikle', ['name', 'id', 'level']) 
                
