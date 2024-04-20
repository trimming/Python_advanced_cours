##В организации есть два типа людей: сотрудники и обычные люди.
##Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
##
##Фамилия(строка, не пустая),
##Имя(строка, не пустая),
##Отчество(строка, не пустая),
##Возраст (целое положительное число).
##Сотрудники имеют также уникальный идентификационный номер (ID),
##который должен быть шестизначным положительным целым числом.
##
##Ваша задача:
##
##Создать класс Person, который будет иметь атрибуты и методы
##для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
##Класс должен проверять валидность входных данных и генерировать
##исключения InvalidNameError и InvalidAgeError, если данные неверные.
##
##Создать класс Employee, который будет наследовать класс Person
##и добавлять уникальный идентификационный номер (ID).
##Класс Employee также должен проверять валидность ID и
##генерировать исключение InvalidIdError, если ID неверный.
##
##Добавить метод birthday в класс Person,
##который будет увеличивать возраст человека на 1 год.
##
##Добавить метод get_level в класс Employee,
##который будет возвращать уровень сотрудника
##на основе суммы цифр в его ID (по остатку от деления на 7).
##
##Создать несколько объектов класса Person и Employee
##с разными данными и проверить, что исключения
##работают корректно при передаче неверных данных.

class Person:
    def __init__(self, surname, first_name, last_name, age):
        if surname != '' and isinstance(surname, str):
            self.surname = surname
        else:
            raise InvalidNameError(f'{surname}')
        if first_name != '' and isinstance(first_name, str):
            self.first_name = first_name
        else:
            raise InvalidNameError(f'{first_name}')
        if last_name != '' and isinstance(last_name, str):
            self.last_name = last_name
        else:
            raise InvalidNameError(f'{last_name}')
        if age > 0 and isinstance(age, int):
            self._age = age
        else:
            raise InvalidAgeError(f'{age}')

    def birthday(self):
        return self._age + 1
    def get_age(self):
        return self._age

class Employee(Person):
    def __init__(self, surname: str, first_name: str, last_name: str, age: int, ID: int):
        if ID > 0 and 100000 <= ID < 1000000:
            self.id = ID
        else:
            raise InvalidIdError(f'{ID}')
        super().__init__(surname, first_name, last_name, age)
        self.level = self.get_level()

    def get_level(self):
        return sum(map(int, str(self.id))) % 7


class InvalidNameError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'Invalid name: {self.message}. Name should be a non-empty string.'


class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'Invalid age: {self.message}. Age should be a positive integer.'


class InvalidIdError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'Invalid id: {self.message}. Id should be a 6-digit positive integer between 100000 and 999999.'


# a = Person('Bdfy', 'ghg', 'Gtnhjd', 4)
# b = Employee(123456, 'Голикова', 'Ева', 'Алексеевна', 6)
# print(a.birthday())
# print(b.level)

# test_1
# person = Person("", "John", "Doe", 30)
# __main__.InvalidNameError: Invalid name: . Name should be a non-empty string.

# test_2
# person = Person("Alice", "Smith", "Johnson", -5)
# __main__.InvalidAgeError: Invalid age: -5. Age should be a positive integer.

# test_3
# employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
# __main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.

# test_4
person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
# 25