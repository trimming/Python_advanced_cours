##Задание №1
##✔ Напишите функцию, которая заполняет файл
##(добавляет в конец) случайными парами чисел.
##✔ Первое число int, второе - float разделены вертикальной чертой.
##✔ Минимальное число - -1000, максимальное - +1000.
##✔ Количество строк и имя файла передаются как аргументы функции.

import random as rd
##def fill_file(num_lines: int, file_name: str):
##    with open(file_name, 'w+', encoding='utf-8') as f:
##        for i in range(num_lines):
##            res = f.write(f'{rd.randrange(-1000, 1000)} | {rd.uniform(-1000, 1000)}\n')
##            print(res)
##
##fill_file(5, 'test.txt')        

##Задание №2
##✔ Напишите функцию, которая генерирует
##псевдоимена.
##✔ Имя должно начинаться с заглавной буквы,
##состоять из 4-7 букв, среди которых
##обязательно должны быть гласные.
##✔ Полученные имена сохраните в файл.


##def gen_name():
##    name = ''
##    name_len = rd.randint(4, 7)
##    vow_letter = 'аеёиоуэюя'
##    con_letter = 'бвгджзйклмнпрстфхцчшщъь'
##    all_letter = 'абвгдеёжзийклмнпорстуфхцчшщъьэюя'
##    for i in range(name_len):
##        if len(name) > 1:
##            if name[-1] in vow_letter:
##                name += rd.choice(con_letter)
##            else:
##                name += rd.choice(vow_letter)
##        else:
##            name += rd.choice(all_letter)
##    return name.capitalize()
##
##with open('names.txt', 'a+', encoding='utf-8') as f:
##    for _ in range(4):
##        f.write(f'{gen_name()}\n')

##Задание №3
##✔ Напишите функцию, которая открывает на чтение созданные
##в прошлых задачах файлы с числами и именами.
##✔ Перемножьте пары чисел. В новый файл сохраните
##имя и произведение:
##✔ если результат умножения отрицательный, сохраните имя
##записанное строчными буквами и произведение по модулю
##✔ если результат умножения положительный, сохраните имя
##прописными буквами и произведение округлённое до целого.
##✔ В результирующем файле должно быть столько же строк,
##сколько в более длинном файле.
##✔ При достижении конца более короткого файла,
##возвращайтесь в его начало.
    

    
##def read_files():
##    with open('names.txt', 'r', encoding='utf-8') as f1, \
##          open('test.txt', 'r', encoding='utf-8') as f2, \
##          open('result.txt', 'w+', encoding='utf-8') as f3:
##        num_list = [i[:-2].split('|') for i in list(f2)]
##        for i in num_list:
##            f3.write(f'{int(i[0]) * float(i[1])}\n')
##        print(num_list)
##        
##          
##
##read_files()

##Задание №4
##✔ Создайте функцию, которая создаёт файлы с указанным расширением.
##Функция принимает следующие параметры:
##✔ расширение
##✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
##✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
##✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
##✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
##✔ количество файлов, по умолчанию 42
##✔ Имя файла и его размер должны быть в рамках переданного диапазона


def 















