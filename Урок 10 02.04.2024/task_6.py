from task_5 import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, voice: str):
        super().__init__(name, age, voice)
        self.voice = voice


class Fish(Animal):
    def __init__(self, name: str, age: int, dive_depth: float):
        super().__init__(name, age, dive_depth)
        self.dive_depth = dive_depth


class Bird(Animal):
    def __init__(self, name: str, age: int, speed: float):
        super().__init__(name, age, speed)
        self.speed = speed


if __name__ == '__main__':
    doggy = Dog('Kim', 3, 'bark')
    fishy = Fish('Dori', 1, 1.2)
    birdy = Bird('Kesha', 5, 15)

    print(doggy.spec)
    print(doggy.specific_property())
    print(doggy)