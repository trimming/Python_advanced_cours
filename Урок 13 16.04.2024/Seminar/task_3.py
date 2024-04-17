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
        super().__init__(f'Ошибка доступа: {value}')


class AccessError(UserException):
    def __init__(self, name: str, u_id: str):
        super().__init__(f'Пользователя с таким именем ({name}) и ID({u_id}) не существует')


raise LevelError(4)
