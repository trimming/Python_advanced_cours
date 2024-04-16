# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class UserException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f'Ошибка приложения! {self.msg}'


class LevelError(UserException):
    def __init__(self, value: int):
        super().__init__(f'Неверное значение: {value}')


class AccessError(UserException):
    def __init__(self, level: str):
        super().__init__(f'Ошибка доступа: {level}')


raise LevelError(4)
