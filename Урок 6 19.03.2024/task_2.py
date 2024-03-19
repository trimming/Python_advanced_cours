'''Модуль угадай число в заданном диапазоне с определенным числом попыток'''

from random import randint
from sys import argv


def gen_num(from_num: int, before_num: int, count=3) -> bool:
    result = randint(from_num, before_num)
    while count > 0:
        count -= 1
        user_num = int(input(f'Попробуйте угадать число от {from_num} до {before_num}:\n'))
        if user_num > result:
            print('Меньше')
        elif user_num < result:
            print('Больше')
        else:
            return True
    else:
        return False


args = [int(i) for i in argv if i.isdigit()]
print(gen_num(*args))

# if __name__ == '__main__':
#     print(gen_num(1, 100, 3))
