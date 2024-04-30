# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
import os


def rename_files(desired_name, num_digits, source_ext, target_ext):
    folder_name = 'test_folder'
    folder_path = os.path.join(os.getcwd(), folder_name)
    count = 1
    for file in os.listdir(folder_path):
        file_name_list = file.split('.')
        if len(file_name_list) > 1 and file_name_list[1] == source_ext:
            new_file = f'{desired_name + str(count).zfill(num_digits)}.{target_ext}'
            os.rename(f'{folder_path}\\{file}', f'{folder_path}\\{new_file}')
            os.path.isfile(new_file)
            count += 1


rename_files('new_file_', 3, 'txt', 'doc')
