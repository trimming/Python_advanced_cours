# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import re


def remove_chars(text: str) -> str:
    """
    >>> remove_chars('python forever')
    'python forever'

    >>> remove_chars('Python Forever')
    'python forever'

    >>> remove_chars('python, forever!')
    'python forever'

    >>> remove_chars('Даpython этоforever')
    'python forever'

    >>> remove_chars('Да,Python, этоForever!')
    'python forever'
    """
    letters = re.compile(r'[^a-zA-Z\s]')
    data = re.sub(letters, '', text).lower()
    return data

# user_text = ''
# a = remove_chars(user_text)
# print(a)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)