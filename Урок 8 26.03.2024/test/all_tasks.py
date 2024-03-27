##Задание №1#################################################################
##Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
##текстовый файл с псевдо именами и произведением чисел.
##Напишите функцию, которая создаёт из созданного ранее
##файла новый с данными в формате JSON.
##Имена пишите с большой буквы.
##Каждую пару сохраняйте с новой строки.

##import shutil
##import json
##
####shutil.copy('D:\\GB\\Python погружение\\Python_advanced_cours\\Урок 7 22.03.2024\\result.txt',
####            'D:\\GB\\Python погружение\\Python_advanced_cours\\Урок 8 26.03.2024')
##
##
##def get_dict(file):
##    my_dict = {}
##    with open(file, 'r', encoding='utf-8') as f:
##        while res := f.readline():
##            key, value = res.split(' ')
##            my_dict[key.capitalize()] = value
##    return my_dict
##
##
##def create_json(file, new_file):
##    temp_dict = get_dict(file)
##    with open(new_file, 'w', encoding='utf-8') as fj:
##        json.dump(temp_dict, fj, ensure_ascii=False)
##
##
##create_json('result.txt', 'result.json')

# Задание №2##################################################################
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

##import uuid
##import json
##import random
##
##
##def create_json(file, count):
##    user_dict = {}
##    with open(file, 'r', encoding='utf-8') as r_file:
##        user_dict = json.load(r_file)
##    with open(file, 'w+', encoding='utf-8') as w_file:                
##        while count > 0:
##            user_name = input('Введите, пожалуйста, имя:\n')
##            user_id = str(uuid.uuid4())
##            acc_level = random.randint(1, 7)
##            user_dict.setdefault(acc_level, {}).update({user_id: user_name})
##            json.dump(user_dict, uf, ensure_ascii=False)
##            print(user_dict)
##            count -= 1
##
##create_json(5)            

##Задание №3##############################################################
##Напишите функцию, которая сохраняет созданный в
##прошлом задании файл в формате CSV.        

##import csv
##import json
##
##
##def save_csv(file='_users.json', new_file='_users.csv'):
##    user_dict = {}
##    with open(file, 'r', encoding='utf-8') as r_file:
##        user_dict = json.load(r_file)
##    print(user_dict)
##    with open(new_file, 'w', encoding='utf-8') as cvs_f:
##        user_dict.writerider(cvs_f)
##
##save_csv()    


##Задание №4#################################################################
##Прочитайте созданный в прошлом задании csv файл без
##использования csv.DictReader.
##Дополните id до 10 цифр незначащими нулями.
##В именах первую букву сделайте прописной.
##Добавьте поле хеш на основе имени и идентификатора.
##Получившиеся записи сохраните в json файл, где каждая строка
##csv файла представлена как отдельный json словарь.
##Имя исходного и конечного файлов передавайте как аргументы
##функции.    








        
