class MyDirError(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f'Путь {self.msg} не найден!'