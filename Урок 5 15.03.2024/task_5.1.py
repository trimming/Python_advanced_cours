# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.



gen = (expr for expr in range(1, 101, 3) if condition1
for expr in sequense2 if condition2
for expr in sequense3 if condition3

for expr in sequenseN if conditionN)

res = ("fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101))
print(*res)


data = [[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]]

new_data = [i for item in data for inner in item for i in inner]

n_data = []
for item in data:
    for inner in item:
        for i in inner:
          n_data.append(i)
print(new_data)