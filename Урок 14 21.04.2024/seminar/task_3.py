# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import unittest
import re
from task_1 import remove_chars
class TestCaseName(unittest.TestCase):
    def test_no_changes(self):
        self.assertEqual('python forever', remove_chars('python forever'))

    def test_up_low(self):
        self.assertEqual('python forever', remove_chars('Python Forever'))

    def test_not_punctuation(self):
        self.assertNotEqual('python, forever!', remove_chars('python, forever!'))

    def test_other_lang(self):
        self.assertEqual('python forever', remove_chars('Даpython этоforever'))

    def test_all_variant(self):
        self.assertEqual('python forever', remove_chars('Да,Python, этоForever!'))

if __name__ == '__main__':
    unittest.main(verbosity=2)