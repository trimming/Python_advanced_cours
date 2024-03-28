# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json

def new_user_json(input_file_name: str, output_file_name: str):
    with open(input_file_name,'r', encoding='utf-8', newline='') as in_csv_data, \
        open(output_file_name, 'w', encoding='utf-8') as out_json_file:
        data = {}
        csv_reader = csv.reader(in_csv_data)
        for i, row in enumerate(csv_reader):
            if i:
                user_data = [row[0].lower(), row[1].zfill(10), row[2]]                
                data[hash(user_data[0] + user_data[1])] = user_data
        json.dump(data, out_json_file, indent=4, ensure_ascii=False, sort_keys=True) 

new_user_json('users_list.csv', 'res.json')
