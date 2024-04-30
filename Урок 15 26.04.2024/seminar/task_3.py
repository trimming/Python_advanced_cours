##Задание №3
##Доработаем задачу 2.
##Сохраняйте в лог файл раздельно:
##○ уровень логирования,
##○ дату события,
##○ имя функции (не декоратора),
##○ аргументы вызова,
##○ результат.


import logging

FORMAT = '{levelname:10}\n{asctime:20}\n{name}\n{msg}'
logging.basicConfig(format=FORMAT, style='{', filename='log.log', filemode='a+', level=logging.INFO, encoding='utf-8')
# logger = logging.getLogger(__name__)


def log_info(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__)
        result = func(*args, **kwargs)
        file_data = f'{result}: {args}, {kwargs}'
        logger.info(file_data)
        return result

    return wrapper


@log_info
def tes(a, b):
    return a + b


print(tes(5, b=6))
