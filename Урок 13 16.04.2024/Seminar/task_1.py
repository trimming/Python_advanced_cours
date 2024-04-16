# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def user_input():
    while True:
        try:
            num = float(input('Введите число: \n'))
            if int(num) == num:
                return int(num)
            return num
        except ValueError as e:
            print(f'Ваш ввод привел к ошибке ValueError: {e}')


if __name__ == '__main__':
    n = user_input()
    print(f'Вы ввели: {n = }')
