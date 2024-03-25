# Напишите функцию, которая открывает
# на чтение созданные в прошлых задачах
# файлы с числами и именами. Перемножьте пары чисел.

# В новый файл сохраните имя и произведение:
#   если результат умножения отрицательный,
#   сохраните имя записанное строчными буквами и произведение по модулю

#   если результат умножения положительный,
#   сохраните имя прописными буквами и произведение округлённое до целого.

# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле. При достижении конца
# более короткого файла, возвращайтесь в его начало.


def read_numbers_and_names(file_numbers, file_names, output_file):
    with (open(file_numbers, "r", encoding='utf-8') as file_num,
          open(file_names, 'r', encoding='utf-8') as file_name,
          open(output_file, 'w', encoding='utf-8') as file_output
          ):
        number = sum(1 for i in file_num)
        names = sum(1 for i in file_name)
        for line in range(max(number, names)):
            num1, num2 = process_file(file_num).split('|')
            nam1 = process_file(file_name)
            result = int(num1) * float(num2)
            if result < 0:
                file_output.write(f'{nam1.lower()} {abs(result)}\n')
            else:
                file_output.write(f'{nam1.upper()} {round(result)}\n')


def process_file(file):
    text_res = file.readline()
    if not text_res:
        file.seek(0)
        text_res = file.readline()
    return text_res.strip()


read_numbers_and_names('test.txt', 'names.txt', 'result.txt')
