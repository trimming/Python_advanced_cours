##Напишите функцию для транспонирования матрицы transposed_matrix,
##принимает в аргументы matrix, и возвращает транспонированную матрицу.

matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]


# Введите ваше решение ниже
def transpose(matrix):
    x = [tuple(i) for i in matrix]            
    z = [list(i) for i in zip(*x)]     
    return(z)
transposed_matrix = transpose(matrix)
print(transposed_matrix)






##def transpose(matrix):
##    # определяем количество строк и столбцов в матрице
##    rows = len(matrix)
##    cols = len(matrix[0])
##
##    # создаем новую матрицу с размерами, поменянными местами
##    transposed = [[0 for row in range(rows)] for col in range(cols)]
##
##    # заполняем новую матрицу значениями из старой матрицы
##    for row in range(rows):
##        for col in range(cols):
##            transposed[col][row] = matrix[row][col]
##
##    return transposed
