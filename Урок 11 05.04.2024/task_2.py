# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    arch = []

    # def __new__(cls, *args):
    #     instance = super().__new__(cls)
    #     instance.arch = cls.arch.copy()
    #     cls.arch.append(instance)
    #     return instance

    def __init__(self, number, letter):
        Archive.arch.append([number, letter])
        self.number = number
        self.letter = letter

    def __repr__(self):
        return f'{self.number} {self.letter}'

        def __str__(self):
            return f'STR: {self.number} {self.letter}'

        def __repr__(self):
            return f'REPR: {self.number} {self.letter}'

a = Archive(1, 'a')
b = Archive(2, 'b')

print(a.__repr__())
print(b)
c = [a, b]
print(str(c))

a = Archive(1, 'a')
b = Archive(2, 'b')
# c = Archive(3, 'c')
# d = Archive(4, 'd')

print(a.arch)
print(b.arch)
# print(c.arch)
# print(d.arch)