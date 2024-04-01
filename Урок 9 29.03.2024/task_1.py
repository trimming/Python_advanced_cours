import random
from typing import Callable


def counter(min_number, max_number, count) -> Callable:
    random_num = random.randint(min_number, max_number)
    print(f'Отгадай число от {min_number} до {max_number}, у тебя {count} попыток')

    def checker():
        for _ in range(count):
            user_answer = int(input('Введите число'))
            if user_answer == random_num:
                print('Ура!')
            elif user_answer < random_num:
                print('Меньше')
            else:
                print('Больше')
        print('Попытки закончились')

    return checker


MIN_NUM = 1
MAX_NUM = 100
COUNT = 3
result = counter(MIN_NUM, MAX_NUM, COUNT)
result()
