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
    def __init__(self, my_level: int, new_level: int):
        super().__init__(f'Ошибка доступа! Уровень нового пользователя ({new_level}) меньше вашего уровня ({my_level})')


class AccessError(UserException):
    def __init__(self, name: str, u_id: str):
        super().__init__(f'Пользователя с таким именем ({name}) и ID({u_id}) не существует')


class IdError(UserException):
    def __init__(self, u_id: str):
        super().__init__(f'Пользователя с таким ID({u_id}) уже существует')



    
##raise LevelError(4)
