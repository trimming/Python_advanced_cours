# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime
from exc import *


def check_date(date_str: str):
    year = datetime.today().year

    def _is_leap(cur_year: int) -> bool:
        return bool(not cur_year % 4 and cur_year % 100 or not cur_year % 400)

    week_days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    months = {
        'янв': (31, 1),
        'фев': (29 if _is_leap(year) else 28, 2),
        'мар': (31, 3),
        'апр': (30, 4),
        'май': (31, 5),
        'мая': (31, 5),
        'июн': (30, 6),
        'июл': (31, 7),
        'авг': (31, 8),
        'сен': (30, 9),
        'окт': (31, 10),
        'ноя': (30, 11),
        'дек': (31, 12)
    }
    day, week_day, cur_month = date_str.split()
    day = ''.join([i for i in day if i.isdigit()])

    if cur_month[:3] not in months:
        raise WrongMonth(cur_month)
    month = months[cur_month[:3]]
    if week_day not in week_days:
        raise WrongWeekDay(week_day)

    if day and 0 < int(day) <= 5:
        cur_day, day = int(day), int(day)
    else:
        raise WrongNumber(cur_month, day, week_day)
    cur_weekday, week_day = week_day, week_days.index(week_day)
    first_day = datetime.strptime(f'01-{str(month[1]).zfill(2)}-{year}', '%d-%m-%Y').weekday()
    # print(week_days[first_day])
    for i in range(month[0]):
        if (first_day + i) % 7 == week_day:
            if day == 1:
                return f'{i + 1} {cur_month} {year}'
            else:
                day -= 1
    else:
        return WrongNumber(cur_month, cur_day, cur_weekday)


print(check_date('2-й четверг апреля'))
