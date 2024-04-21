# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest
from task_1 import remove_chars


def test_not_changes():
    assert 'python forever' == remove_chars('python forever')

def test_up_low():
        assert 'python forever' == remove_chars('Python Forever')

def test_not_punctuation():
        assert 'python forever' == remove_chars('python, forever!')

def test_other_lang():
        assert 'python forever' == remove_chars('Даpython этоforever')

def test_all_variant():
        assert 'python forever' == remove_chars('Да,Python, этоForever!')

if __name__ == '__main__':
    pytest.main(['-v'])
