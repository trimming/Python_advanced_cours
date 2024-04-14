# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

class Factorial:
    def __init__(self, k):
        self.k = k
        self._history = []

    def __call__(self, value):
        fact = 1
        for i in range(1, value + 1):
            fact *= i
        self._history.append((value, fact))
        self._history = self._history[-self.k:]
        return fact

    @property
    def history(self):
        return self._history


f = Factorial(3)
print(f(5))
print(f(7))
print(f(2))
print(f(4))
print(f(10))
print(f.history)
