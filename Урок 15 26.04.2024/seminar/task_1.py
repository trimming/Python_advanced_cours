##Задание №1
##Напишите программу, которая использует модуль logging для
##вывода сообщения об ошибке в файл.
##Например отлавливаем ошибку деления на ноль.

import logging

def logging_info(file_name: str, error_msg):
    logging.basicConfig(filename=file_name,
                        filemode='w',                        
                        level=logging.INFO,
                        format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
                        style='{'
                        )
    
    logger = logging.getLogger('__main__')
    logger.info(error_msg)


def user_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging_info('task_1.log', str(e))
    
user_div(5, 0)
