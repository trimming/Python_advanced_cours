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


def new_user_json(input_file_name: str, output_file_name: str):
    with(
        open(input_file_name,'r', encoding='utf-8') as input_csv_data,
        open(output_file_name, 'w', encoding='utf-8') as output_json_file
    ):
        data = []
        csv_reader = csv.reader(input_csv_data)
        for i, row in enumerate(csv_reader):
            if i:
                data.append(row)
        print(data)

new_user_json()