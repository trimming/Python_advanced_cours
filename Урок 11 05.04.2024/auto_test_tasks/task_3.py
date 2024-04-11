class Rectangle:
    """
        Класс, представляющий прямоугольник.

        Атрибуты:
        - width (int): ширина прямоугольника
        - height (int): высота прямоугольника

        Методы:
        - perimeter(): вычисляет периметр прямоугольника
        - area(): вычисляет площадь прямоугольника
        - __add__(other): определяет операцию сложения двух прямоугольников
        - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
        - __lt__(other): определяет операцию "меньше" для двух прямоугольников
        - __eq__(other): определяет операцию "равно" для двух прямоугольников
        - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
        - __str__(): возвращает строковое представление прямоугольника
        - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
        """
    def __init__(self, width, height = None):
        self.width = width
        self.height = height if height else width

    def perimeter(self):
        """Вычисляет периметр прямоугольника.
           Возвращает: - int: периметр прямоугольника"""
        return int((self.height + self.width) * 2)

    def area(self):
        """Вычисляет площадь прямоугольника.
            Возвращает: - int: площадь прямоугольника"""
        return int(self.height * self.width)

    def __add__(self, other):
        """Определяет операцию сложения двух прямоугольников.
            Аргументы:
               - other (Rectangle): второй прямоугольник
               Возвращает:
               - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников"""
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        else:
            raise TypeError('Ошибка класса!')

    def __sub__(self, other):
        """Определяет операцию вычитания одного прямоугольника из другого.
            Аргументы:
               - other (Rectangle): вычитаемый прямоугольник
            Возвращает:
               - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного"""
        if isinstance(other, Rectangle):
            new_perimetr = abs(self.perimeter() - other.perimeter())
            new_height = (new_perimetr / 2) // 2
            new_width = (new_perimetr / 2) - new_height
            return Rectangle(int(new_height), int(new_width))
        else:
            raise TypeError('Ошибка класса!')

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise TypeError('Ошибка класса!')

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            raise TypeError('Ошибка класса!')

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()
        else:
            raise TypeError('Ошибка класса!')

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'


if __name__ == '__main__':
    r1 = Rectangle(4, 5)
    r2 = Rectangle(8, 8)
    print(r1 < r2)