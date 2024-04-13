class Matrix:
    """
        Класс, представляющий матрицу.

        Атрибуты:
        - rows (int): количество строк в матрице
        - cols (int): количество столбцов в матрице
        - data (list): двумерный список, содержащий элементы матрицы

        Методы:
        - __str__(): возвращает строковое представление матрицы
        - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
        - __eq__(other): определяет операцию "равно" для двух матриц
        - __add__(other): определяет операцию сложения двух матриц
        - __mul__(other): определяет операцию умножения двух матриц
        """
    count = 0

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        # self.data = [[0 for _ in range(self.cols)] for _ in range(rows)]
        self.data = self.create_data()

    def create_data(self):
        data = []
        for i in range(self.rows):
            in_data = []
            for _ in range(self.cols):
                Matrix.count += 1
                in_data.append(Matrix.count)
            data.append(in_data)
        return data

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        Возвращает:
        - str: строковое представление матрицы
        """
        line = ''
        for row in self.data:
            row = [str(i) for i in row]
            line += ' '.join(row) + '\n'

    def __repr__(self):
        """
        Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление матрицы
        """
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - bool: True, если матрицы равны, иначе False
        """
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols and self.__str__() == other.__str__():
                return True
            else:
                return False
        else:
            raise TypeError('Ошибка класса!')

    def __add__(self, other):
        """
        Определяет операцию сложения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем сложения двух исходных матриц
        """
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                new_matrix = Matrix(self.rows, self.cols)
                new_matrix.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in
                                   range(self.rows)]
                return new_matrix
        else:
            raise TypeError('Ошибка класса!')

    def __mul__(self, other):
        """
        Определяет операцию умножения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем умножения двух исходных матриц
        """
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                new_matrix = Matrix(other.rows, self.cols)
                new_matrix.data = []
                if self.rows > other.rows:
                    for i in range(self.rows):
                        item_data = []
                        for j in range(other.rows):
                            el = 0
                            for k in range(other.rows):
                                el += other.data[k][j] * self.data[i][k]
                            item_data.append(el)
                        new_matrix.data.append(item_data)
                    return new_matrix
                else:
                    for i in range(other.rows):
                        item_data = []
                        for j in range(self.rows):
                            el = 0
                            for k in range(self.rows):
                                el += self.data[k][j] * other.data[i][k]
                            item_data.append(el)
                        new_matrix.data.append(item_data)
                    return new_matrix
        else:
            raise TypeError('Ошибка класса!')


##mx = Matrix(3, 2)
##mx2 = Matrix(2, 3)
##print(mx)
##print(mx2)
##print(mx * mx2)


matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(2, 2)
matrix3.data = [[1, 2], [3, 4]]

matrix4 = Matrix(2, 3)
matrix4.data = [[7, 8, 9], [9, 10, 2], [5, 6, 1]]

result = matrix3 * matrix4
print(result)
