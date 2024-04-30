##Задание №4
##Создайте декоратор с параметром.
##Параметр - целое число, количество запусков декорируемой
##функции.





from functools import wraps


def counter(count: int):
    def deco(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return deco

