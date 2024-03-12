from random import randint

print(my_list := [randint(1, 10) for _ in range(10)])

# [print(i, end=', ') for i, value in enumerate(my_list, 1) if value % 2]

for i, value in enumerate(my_list, 1):
    if value % 2:
        print(i, end=' ')