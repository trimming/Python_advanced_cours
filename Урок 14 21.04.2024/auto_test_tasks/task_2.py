import unittest

class NegativeValueError(ValueError):
    pass


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(5.0)
        self.rect2 = Rectangle(3.0, 4.0)
        
    def test_width(self):
        self.assertEqual(5.0, self.rect1.width)

    def test_height(self):
        self.assertEqual(4.0, self.rect2.height)

    def test_perimeter(self):
        self.assertEqual(20.0, self.rect1.perimeter())

    def test_area(self):
        self.assertEqual(12.0, self.rect2.area())

    def test_addition(self):
        self.r3 = self.rect1 + self.rect2
        self.assertEqual(8.0, self.r3.width)
        self.assertEqual(6.0, self.r3.height)


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

if __name__ == '__main__':
    unittest.main(verbosity=2)    
