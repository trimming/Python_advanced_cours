# Вы работаете над разработкой программы для проверки корректности даты,
# введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.


def _is_leap(year):
    return True if not year % 400 or not year % 4 and year % 100 else False


def validate_date(user_date):
    day, month, year = map(int, user_date.split('.'))
    month_dict = {}
    for i in range(1, 13):
        if i in (4, 6, 9, 11):
            month_dict[i] = 30
        elif i == 2:
            if _is_leap(year):
                month_dict[i] = 29
            else:
                month_dict[i] = 28
        else:
            month_dict[i] = 31
    if 0 < year < 10000 and month in month_dict and 0 < day <= month_dict[month]:
        return True
    return False


date_to_prove = '01.02.2024'
print(validate_date(date_to_prove))
