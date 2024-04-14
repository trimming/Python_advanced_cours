# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class FactorialGen:
    def __init__(self, *args):
        self.start, self.stop, self.step = 1, 1, 1
        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
        elif len(args) == 3:
            self.start, self.stop, self.step = args
        else:
            raise ValueError

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        while self.start <= self.stop + self.step:
            return self.factorial(self.start - self.step)
        raise StopIteration

    def factorial(self, num):
        count = 1
        for n in range(1, num + 1):
            count = count * n
        return count


fact = FactorialGen(4)
for i in fact:
    print(i)
