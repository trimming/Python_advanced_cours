from datetime import datetime

birthday = '10.01.2011'

b_day = datetime.strptime(birthday, '%d.%m.%Y')

print(datetime.now().year - b_day.year)