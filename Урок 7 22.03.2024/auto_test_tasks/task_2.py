
with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write('''def rename_files(desired_name, num_digits, source_ext, target_ext):
    folder_name = 'test_folder'    
    folder_path = os.path.join(os.getcwd(), folder_name)
    count = 1
    for file in os.listdir(folder_path):
        file_name_list = file.split('.')
        if len(file_name_list) > 1 and file_name_list[1] == source_ext:
            new_file = f'{desired_name + str(count).zfill(num_digits)}.{target_ext}'
            os.rename(f'{folder_path}/{file}', f'{folder_path}/{new_file}')
            os.path.isfile(new_file)
            count += 1''')