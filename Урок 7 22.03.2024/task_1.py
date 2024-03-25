import random

M_NUM = -1000
MAX_NUM = 1000


def num_random(num, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(num):
            int_num = random.randint(M_NUM, MAX_NUM)
            float_num = random.uniform(M_NUM, MAX_NUM)
            file.write(f'{int_num}|{float_num}\n')


num_random(3, 'num_random.txt')
with open('num_random.txt', 'r', encoding='utf-8') as f:
    [print(i) for i in f]
