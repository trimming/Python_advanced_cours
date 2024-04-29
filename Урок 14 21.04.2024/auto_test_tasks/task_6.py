import pytest


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


# Введите ваше решение ниже
class TestEmployee:
    def test_employee_full_name(self):
        """
        Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov",
        именем "Ivan", отчеством "Ivanovich" и убедитесь,
        что метод full_name() возвращает правильное полное имя в формате "Ivanov Ivan Ivanovich".
        """
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        assert 'Ivanov Ivan Ivanovich' == emp.full_name()

    def test_employee_birthday(self):
        """
        Тестирование метода birthday(). Создайте объект Employee с возрастом 30,
        вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.
        """
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        emp.birthday()
        assert 31 == emp.get_age()

    def test_employee_raise_salary(self):
        """
        Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000,
        вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.
        """
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        emp.raise_salary(10)
        assert 55000.0 == emp.salary

    def test_employee_str(self):
        """
        Тестирование метода __str__(). Создайте объект Employee
        с данными: фамилия "Ivanov", имя "Ivan", отчество "Ivanovich",
        возраст 30, должность "manager" и зарплата 50000. Убедитесь,
        что метод __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".
        """
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        assert 'Ivanov Ivan Ivanovich (Manager)' == str(emp)
    def test_employee_last_name_title(self):
        """
        Тестирование атрибута last_name. Создайте объект Employee с фамилией "Ivanov" и убедитесь,
        что атрибут last_name возвращается в верхнем регистре, то есть "Ivanov".
        """
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        assert 'Ivanov' == emp.last_name


if __name__ == '__main__':
    pytest.main(['-v'])