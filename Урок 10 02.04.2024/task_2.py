# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, lenght, width=None) -> None:
        self.lenght = lenght
        self.width = width if width else lenght

    def perimeter(self):
        return 2 * (self.width + self.lenght)

    def area(self):
        return self.width * self.lenght


rec = Rectangle(4, 10)
rec_sq = Rectangle(5)

print(rec.area(), rec.perimeter(), sep="\n")
print(rec_sq.area(), rec_sq.perimeter(), sep="\n")
