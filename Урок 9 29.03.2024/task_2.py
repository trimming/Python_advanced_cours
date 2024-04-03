##Задание №2
##Дорабатываем задачу 1.
##Превратите внешнюю функцию в декоратор.
##Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
##Если не входят, вызывать функцию со случайными числами
##из диапазонов
from functools import wraps
import random
from typing import Callable
import task_3
import task_4


def validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num = args[0]
        attempts = args[1]
        if not 0 < num < 101:
            num = random.randint(1, 100)
        if not 0 < attempts < 11:
            attempts = random.randint(1, 10)
        return func(num, attempts)

    return wrapper


@task_4.counter(2)
@task_3.writer_json
@validator
def user_quest(num, count):
    print(f'Отгадай число от 1 до 100, у тебя {count} попыток')
    for _ in range(count):
        user_answer = int(input('Введите число: \n'))
        if user_answer == num:
            print('Ура!')
        elif user_answer < num:
            print('Больше')
        else:
            print('Меньше')
    print(f'Попытки закончились. Было загадано {num}')
    return num


if __name__ == '__main__':
    user_quest(120, 2)
