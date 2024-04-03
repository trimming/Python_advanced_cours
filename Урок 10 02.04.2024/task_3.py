# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Human:
    def __init__(
        self, last_name: str, name: str, patronymic: str, age: int, gender: str
    ) -> None:
        self.last_name = last_name
        self.name = name
        self.patronymic = patronymic
        self._age = age
        self.gender = gender

    def birthday(self):
        self._age += 1

    def full_name(self) -> str:
        return f"{self.last_name} {self.name} {self.patronymic}"


man1 = Human("Иванов", "Иван", "Иванович", 25, "муж")
print(man1.full_name(), man1._age)
man1.birthday()
print(man1._age)