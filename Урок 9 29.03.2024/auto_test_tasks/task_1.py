import json
import csv
import random

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.writer(f_write, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(rows):
            csv_write.writerow([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])

def find_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D = 0:
        return - (b / (2 * a))
    else:
        return (((-b + D ** 0.5) / (2 * a)), ((-b + D ** 0.5) / (2 * a)))
        

            

generate_csv_file('input_data.csv', 101)            
