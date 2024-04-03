class Animal:
    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    def __init__(self, name: str, wingspan: float):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: float):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        else:
            return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'


class AnimalFactory:

    def create_animal(self: str, *args):

        if self == 'Bird':
            return Bird(*args)
        elif self == 'Fish':
            return Fish(*args)
        elif self == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')


animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Krish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

print(animal1.wing_length())
print(animal2)
print(animal3.category())
