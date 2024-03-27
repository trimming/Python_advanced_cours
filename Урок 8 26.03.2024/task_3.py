# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv


def convert_to_csv(json_file, csv_file):
    with (
        open(json_file, 'r', encoding='utf-8') as user_json,
        open(csv_file, 'w', encoding='utf-8') as user_csv
    ):
        data = json.load(user_json)
        csv_writer = csv.writer(user_csv)
        csv_writer.writerow(['name', 'ID', 'level'])
        for user_lvl, user in data.items():
            for user_id, user_name in user.items():
                csv_writer.writerow([user_name, user_id, user_lvl])


convert_to_csv('users_list.json', 'users_list.csv')
