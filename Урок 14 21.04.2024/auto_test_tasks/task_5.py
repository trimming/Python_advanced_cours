import pytest


class NegativeValueError(ValueError):
    pass


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


# Введите ваше решение ниже

def test_width():
    r = Rectangle(5)
    assert r._width == 5


def test_height():
    r = Rectangle(3, 4)
    assert 4 == r._height


def test_perimeter():
    r = Rectangle(5)
    assert 20 == r.perimeter()


def test_area():
    r = Rectangle(3, 4)
    assert 12 == r.area()


def test_addition():
    r1 = Rectangle(5, 1)
    r2 = Rectangle(3, 4)
    r3 = r1 + r2
    assert 8 == r3._width
    assert 4 == r3._height


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)


def test_set_width():
    r = Rectangle(5)
    r.width = 10
    assert r._width == 10


def test_set_negative_width():
    with pytest.raises(NegativeValueError):
        r = Rectangle(5)
        r.width = -10


def test_set_height():
    r = Rectangle(3, 4)
    r.height = 6
    assert r._height == 6


def test_set_negative_height():
    with pytest.raises(NegativeValueError):
        r = Rectangle(3, 4)
        r.height = -6


def test_subtraction():
    with pytest.raises(NegativeValueError):
        r1 = Rectangle(10, 1)
        r2 = Rectangle(3, 4)
        r3 = r1 - r2



def test_subtraction_negative_result():
    r1 = Rectangle(10, 1)
    r2 = Rectangle(3, 4)
    r3 = r1 - r2
    assert 7 == r3._width
    assert -3 == r3._height

def test_subtraction_same_perimeter():
    r1 = Rectangle(5, 1)
    r2 = Rectangle(4, 3)
    r3 = r1 - r2
    assert 1 == r3._width
    assert 0 == r3._height


if __name__ == '__main__':
    pytest.main(['-v'])
