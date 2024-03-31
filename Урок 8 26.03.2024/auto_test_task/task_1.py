import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path_file = os.path.join(root, file)
            size_file = os.path.getsize(path_file)
            results.append({'Path': path_file, 'Type': 'File', 'Size': size_file})

        for obj in dirs:
            path_dir = os.path.join(root, obj)
            size_dir = get_dir_size(path_dir)
            results.append({'Path': path_dir, 'Type': 'Directory', 'Size': size_dir})
    return results


def get_dir_size(path_obj):
    size_obj = 0
    for root, dirs, files in os.walk(path_obj):
        for file in files:
            path_file = os.path.join(root, file)
            size_obj += os.path.getsize(path_file)
    return size_obj


def save_results_to_json(obj, name_file):
    with open(name_file, 'w', encoding='utf-8') as json_file:
        json.dump(obj, json_file, ensure_ascii=False)


def save_results_to_csv(obj, name_file):
    with open(name_file, 'w', newline='', encoding='utf-8') as write_file:
        csv_write = csv.DictWriter(write_file, fieldnames=['Path', 'Type', 'Size'])
        csv_write.writeheader()
        all_data = []
        for el in obj:
            all_data.append(el)
        csv_write.writerows(all_data)


def save_results_to_pickle(obj, name_file):
    with open(name_file, 'wb') as write_file:
        pickle.dump(obj, write_file)


save_results_to_json(traverse_directory('D:\GB\Python погружение\Python_advanced_cours\Урок 8 26.03.2024'),
                     'lesson_8.json')
save_results_to_csv(traverse_directory('D:\GB\Python погружение\Python_advanced_cours\Урок 8 26.03.2024'),
                    'lesson_8.csv')
save_results_to_pickle(traverse_directory('D:\GB\Python погружение\Python_advanced_cours\Урок 8 26.03.2024'),
                       'lesson_8.pickle')
