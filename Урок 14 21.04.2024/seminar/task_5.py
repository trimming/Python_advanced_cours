# Задание №5
# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest


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


class TestCheckRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(5, 3)
        self.rect2 = Rectangle(4, 4)
        self.rect3 = Rectangle(4, 2)

    def test_perimetr(self):
        self.assertEqual(self.rect1.rectangle_perimeter(), self.rect2.rectangle_perimeter())

    def test_area(self):
        self.assertNotEqual(self.rect1.rectangle_area(), self.rect2.rectangle_area())

    def test_add(self):
        a = self.rect1 + self.rect2
        self.assertTrue(a == Rectangle(7, 9))

    def test_sub(self):
        a = self.rect1 - self.rect3
        self.assertTrue(a == Rectangle(1, 1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
