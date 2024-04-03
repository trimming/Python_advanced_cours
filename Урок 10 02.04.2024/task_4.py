# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from task_3 import Human


class Employee(Human):
    def __init__(
            self, last_name: str, name: str, patronymic: str, age: int, gender: str, id: int
    ) -> None:
        super().__init__(last_name, name, patronymic, age, gender)
        self.id = id if len(str(id)) == 6 else 111111

        # self.level = self.access_level()

    @property
    def access_level(self) -> int:
        acc_lvl = sum(map(int, str(self.id)))
        return acc_lvl % 7


man1 = Employee("Иванов", "Иван", "Иванович", 25, "муж", 789456)

print(man1.access_level)
man1.id = 7777777
print(man1.access_level)
