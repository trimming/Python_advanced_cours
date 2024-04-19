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
            raise InvalidNameError(f'Фамилия должна быть не пустой строкой!')
        if first_name != '' and isinstance(first_name, str):
            self.first_name = first_name
        else:
            raise InvalidNameError(f'Имя должно быть не пустой строкой!')
        if last_name != '' and isinstance(last_name, str):
            self.last_name = last_name
        else:
            raise InvalidNameError(f'Отчество должно быть не пустой строкой!')
        if age > 0 and isinstance(age, int):
            self._age = age
        else:
            raise InvalidAgeError(f'Возраст должен быть целым числом!')
    
    def birthday(self):
        return self._age + 1

class Employee(Person):
    def __init__(self, ID):
        

class InvalidNameError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'{self.message}'

class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'{self.message}'
    

a = Person('Bdfy', 'ghg', 'Gtnhjd', 4)
print(a.birthday())
