import json
import csv
import random

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.writer(f_write, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(rows):
            csv_write.writerow([random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)])

def save_to_json(func):
    def wrapper(*args, **kwargs):
        csv_file = args[0]
        result = []
        with open(csv_file, 'r', newline='') as f_csv:
            csv_read = csv.reader(f_csv, dialect='excel-tab')
            for row in csv_read:
                row = [int(i) for i in ''.join(row).split(',')]
                res = func(row)
                result.append({'parameters': row, 'result': res})
        with open('result.json', 'w', encoding='utf-8') as f_json:
            json.dump(result, f_json, ensure_ascii=False, indent=4)
        
    return wrapper

@save_to_json
def find_roots(*args, **kwargs):
    a = args[0][0]
    b = args[0][1]
    c = args[0][2]
    
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        return -b / (2 * a)
    else:
        return (((-b + D ** 0.5) / (2 * a)), ((-b + D ** 0.5) / (2 * a)))
find_roots('input_data.csv')

            

##generate_csv_file('input_data.csv', 101)            
