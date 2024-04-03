from typing import Any

'''
Создайте три (или более) отдельных классов животных.
Например, рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''


class Animal:
    def __init__(self, name: str, age: int, spec: Any):
        self.name = name
        self.age = age
        self.spec = spec

    def specific_property(self):
        return self.spec

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}'


class Dog:
    def __init__(self, name: str, age: int, voice: str):
        self.name = name
        self.age = age
        self.voice = voice

    def specific_property(self):
        return self.voice

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}'


class Fish:
    def __init__(self, name: str, age: int, dive_depth: float):
        self.name = name
        self.age = age
        self.dive_depth = dive_depth

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}'

    def specific_property(self):
        return self.dive_depth


class Bird:
    def __init__(self, name: str, age: int, speed: float):
        self.name = name
        self.age = age
        self.speed = speed

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}'

    def specific_property(self):
        return self.speed


if __name__ == '__main__':
    doggy = Dog('Kim', 3, 'bark')
    fishy = Fish('Dori', 1, 1.2)
    birdy = Bird('Kesha', 5, 15)
