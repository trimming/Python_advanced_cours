##Задание №3
##Доработаем задачу 2.
##Сохраняйте в лог файл раздельно:
##○ уровень логирования,
##○ дату события,
##○ имя функции (не декоратора),
##○ аргументы вызова,
##○ результат.


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
##45:55
