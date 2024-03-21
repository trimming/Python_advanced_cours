# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая
# расстановка ферзей на шахматной доске, в которой ни один ферзь не бьет другого.
# Другими словами, ферзи размещены таким образом,
# что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.


import random


def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    for i in queens:
        for j in queens:
            if i == j:
                continue
            if is_attacking(i, j):
                return False
    return True


def generate_boards():
    board_list = []
    while True:
        row_list = []
        col_list = [1, 2, 3, 4, 5, 6, 7, 8]
        while len(row_list) < 8:
            i = random.randint(1, 8)
            if i not in row_list:
                row_list.append(i)
        res_list = list(zip(col_list, row_list))
        if check_queens(res_list):
            if res_list not in board_list:
                board_list.append(res_list)
                if len(board_list) == 4:
                    return board_list


print(generate_boards())
