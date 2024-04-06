from datetime import datetime


class MyStr(str):
    """
        Класс для создания строки с информацией об авторе и времени создания.

        Атрибуты:
        value (str): строковое значение.
        author (str): имя автора.

        Dunder методы:
        __new__(cls, value, author): создает новый объект класса.
        __str__(): возвращает строковое представление объекта класса.
        __repr__(): возвращает строковое представление объекта класса для отладки.

    """
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls)
        instance.value = value
        instance.author = author
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


first_line = MyStr('Добро пожаловать!', 'Директор')
print(first_line)
print(repr(first_line))