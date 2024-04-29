##Задание №2
##На семинаре про декораторы был создан логирующий
##декоратор. Он сохранял аргументы функции и результат её
##работы в файл.
##Напишите аналогичный декоратор, но внутри используйте
##модуль logging.

import logging

logging.basicConfig(filename='log.log', level=logging.INFO)

def log_info(func):
    def wrapper(*args, **kwargs):
        logging.info(f'{func.__name__}{args}{kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__}: {result}')
        return result
    return wrapper

@log_info
def test(a, b):
    return a+b
test(5, 6) 
    
