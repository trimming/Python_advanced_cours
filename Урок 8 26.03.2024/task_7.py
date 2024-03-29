##Задание №7
##Прочитайте созданный в прошлом задании csv файл без
##использования csv.DictReader.
##Распечатайте его как pickle строку.



import pickle
import csv
import os


def print_pickle(path_csv: str):
    with open(path_csv, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        data = [row for row in csv_reader]
        print(pickle.dumps(data))

print_pickle('users_list.csv')        
