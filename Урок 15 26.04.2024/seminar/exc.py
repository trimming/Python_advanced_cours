class MyException(Exception):
    def __init__(self, msg:str):
        self.msg = msg

    def __str__(self):
        return self.msg



class WrongMonth(MyException):
    def __init__(self, month):
        super().__init__(f'Месяца {month} не существует!')

class WrongWeekDay(MyException):
    def __init__(self, week_day):
        super().__init__(f'Дня недели {week_day} не существует!')


class WrongNumber(MyException):
    def __init__(self, month, number, week_day):
        super().__init__(f'В {month} нет {number}-го {week_day}!')
