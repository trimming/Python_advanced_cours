# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

class Validator:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return getattr(instance, self.value)

    def __set__(self, instance, value):
        if isinstance(value, int):
            raise TypeError('Значение должно быть целым числом!')
        elif value <= 0:
            raise ValueError('Значение должно быть положительным!')
        else:
            setattr(instance, self.value, value)


class Rectangle:
    __slots__ = ('_length', '_width')
    length = Validator()
    width = Validator()

    def __init__(self, length: float, width: float = None):
        self._length = length
        self._width = width if width else length

    def __add__(self, other: "Rectangle"):
        if isinstance(other, Rectangle):
            new_length = self._length + other._length
            new_width = self._width + other._width
            return Rectangle(new_length, new_width)
        raise TypeError('Ошибка класса')

    def __sub__(self, other: "Rectangle"):
        if isinstance(other, Rectangle):
            if self._length > other._length and self._width > other._width:
                return Rectangle(self._length - other._length,
                                 self._width - other._width)
            raise ValueError('Неправильное соотношение сторон')
        raise TypeError('Ошибка класса')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Rectangle(self._length * other, self._width * other)
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
        return f'length {self._length}, width {self._width}'

    def rectangle_perimeter(self):
        return (self._length + self._width) * 2

    def rectangle_area(self):
        return self._length * self._width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Длина должна быть положительной!')

    @width.setter
    def width(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Ширина должна быть положительной!')


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
    rectangle_2.length = 3
