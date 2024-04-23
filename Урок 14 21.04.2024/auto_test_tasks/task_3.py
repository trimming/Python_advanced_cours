import doctest

class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        """
        >>> e1=Person('Ivanov', 'Ivan', 'Ivanovich', 30)
        >>> e1.full_name()
        'Ivanov Ivan Ivanovich'
        """
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        """
        >>> e1=Person('Ivanov', 'Ivan', 'Ivanovich', 30)
        >>> e1.birthday()
        >>> e1.get_age()
        31
        """
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        """
        >>> e1=Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        >>> e1.last_name
        'Ivanov'
        """
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        
        self.salary *= (1 + percent / 100)

    def __str__(self):
        """
        >>> e1=Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        >>> print(e1)
        Ivanov Ivan Ivanovich (Manager)
        """
        return f'{self.full_name()} ({self.position})'

def test_employee_raise_salary(percent, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
    """
    >>> emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
    >>> emp.raise_salary(10.0)
    >>> emp.salary    
    55000.0
    """
    e1 = Employee(last_name, first_name, patronymic, age, position, salary)
    e1.raise_salary(percent)
    return e1.salary

    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)  


Ожидаемый ответ:

**********************************************************************
, in __main__.test_employee_raise_salary
Failed example:
    emp.salary
Expected:
    55000.0
Got:
    55000.00000000001
**********************************************************************
1 items had failures:
   1 of   3 in __main__.test_employee_raise_salary
***Test Failed*** 1 failures.


Ваш ответ:

**********************************************************************
, in __main__.test_employee_raise_salary
Failed example:
    emp.salary    
Expected:
    55000.0
Got:
    55000.00000000001
**********************************************************************
1 items had failures:
   1 of   3 in __main__.test_employee_raise_salary
***Test Failed*** 1 failures.







