import doctest


class NegativeValueError(Exception):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        """
        >>> r1=Rectangle(5.0)
        >>> r1.width
        5.0
        >>> r2=Rectangle(3.0, 4.0)
        >>> r2.width
        3.0
        >>> r2.height
        4.0
        >>> r3 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2
        >>> r4 = Rectangle(5, -3)
        Traceback (most recent call last):
        ...
        NegativeValueError: Высота должна быть положительной, а не -3
        """

        if width > 0:
            self.width = width
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')

        if height is None:
            self.height = width
        else:
            if height > 0:
                self.height = height
            else:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')

    def perimeter(self):
        """
        >>> r1=Rectangle(5.0)
        >>> r1.perimeter()
        20.0
        >>> r2=Rectangle(3.0, 4.0)
        >>> r2.perimeter()
        14.0
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        >>> r1=Rectangle(5.0)
        >>> r1.area()
        25.0
        >>> r2=Rectangle(3.0, 4.0)
        >>> r2.area()
        12.0
        """
        return self.width * self.height

    def __add__(self, other):
        """
        >>> r1=Rectangle(5.0)
        >>> r2=Rectangle(3.0, 4.0)
        >>> r3=r1+r2
        >>> r3.width
        8.0
        >>> r3.height
        6.0
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        >>> r1=Rectangle(5.0)
        >>> r2=Rectangle(3.0, 4.0)
        >>> r3=r1-r2
        >>> r3.width
        2.0
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            width = abs(self.width - other.width)
            perimeter = self.perimeter() - other.perimeter()
            height = perimeter / 2 - width
            return Rectangle(width, height)

    def __lt__(self, other):

        return self.area() < other.area()

    def __eq__(self, other):

        return self.area() == other.area()

    def __le__(self, other):

        return self.area() <= other.area()

    def __str__(self):

        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):

        return f"Rectangle({self.width}, {self.height})"


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=False)
