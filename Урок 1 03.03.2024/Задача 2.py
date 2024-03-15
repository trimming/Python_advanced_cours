# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное
# и делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
# Если подается отрицательное число или число более ста тысяч, выведите на экран сообщение:
# "Число должно быть больше 1 и меньше 100000".
#
# Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.

num = int(input('Введите число: '))
MIN_NUM = 1
MAX_NUM = 100001
count = 0
if MIN_NUM < num < MAX_NUM:
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count > 0:
        print('Не является простым')
    else:
        print('Простое')
else:
    print('Число должно быть больше 1 и меньше 100000')

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            yield False
    yield True


f = is_prime(12)
for _ in range(10):
    print(next(f))


    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


    def prime_numbers_generator(n):
        num = 2
        count = 0
        while count < n:
            if is_prime(num):
                yield num
                count += 1
            num += 1

def generat_pr(n):
    num = 2
    count = 0
    while count < n:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num
            count += 1
        num += 1
n = 20
for i in generat_pr(n):
    print(i, end=" ")