# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, length: float, width: float = None):
        self.length = length
        self.width = width if width else length

    def __add__(self, other: "Rectangle"):
        if isinstance(other, Rectangle):
            new_length = self.length + other.length
            new_width = self.width + other.width
            return Rectangle(new_length, new_width)
        raise TypeError('Ошибка класса')

    def __sub__(self, other: "Rectangle"):
        if isinstance(other, Rectangle):
            if self.length > other.length and self.width > other.width:
                return Rectangle(self.length - other.length,
                                 self.width - other.width)
            raise ValueError('Неправильное соотношение сторон')
        raise TypeError('Ошибка класса')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Rectangle(self.length * other, self.width * other)
        raise TypeError('Ошибка класса')

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.rectangle_area() == other.rectangle_area()
        raise TypeError('Ошибка класса')

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.rectangle_area() > other.rectangle_area()
        raise TypeError('Ошибка класса')

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.rectangle_area() >= other.rectangle_area()
        raise TypeError('Ошибка класса')

    def __hash__(self):
        return hash(self.rectangle_perimeter())

    def __str__(self):
        return f'length {self.length}, width {self.width}'

    def rectangle_perimeter(self):
        return (self.length + self.width) * 2

    def rectangle_area(self):
        return self.length * self.width


if __name__ == '__main__':
    rectangle_1 = Rectangle(10)
    rectangle_2 = Rectangle(3, 4)
    print(rectangle_1 + rectangle_2)
    print(rectangle_1 - rectangle_2)
    print(rectangle_2 * 5)
    # print(rectangle_2 - rectangle_1)
    rectangle_1 = Rectangle(10)
    rectangle_2 = Rectangle(10, 10)
    print(rectangle_1 == rectangle_2)