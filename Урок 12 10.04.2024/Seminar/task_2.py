# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.
import json
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(self._history, file)


f = Factorial(3)
# print(f(5))
# print(f(7))
# print(f(2))
# print(f(4))
# print(f(10))
# print(f.history)

with f as a:
    print(a(5))
    print(a(2))
    print(a(4))
    print(a(6))