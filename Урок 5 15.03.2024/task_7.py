# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


# def gen_numbers(num, count=0):
#     for i in range(2, num):
#         if num % i != 0:
#             print(num)
#
#
# gen_numbers(100)

# def generat_pr(n):
#     num = 2
#     count = 0
#     while count < n:
#         if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#             yield num
#             count += 1
#         num += 1
#
#
# n = 20
# for i in generat_pr(n):
#     print(i, end=" ")

def func_gen():
    number = 0
    while True:
        number += 1
        if number in (1, 2, 3):
            yield number
            continue
        if not number % 2:
            continue
        for dev in range(3, int(number ** 0.5) + 1, 2):
            if not number % dev:
                break
        else:
            yield number


gen = func_gen()

for _ in range(100):
    print(next(gen))