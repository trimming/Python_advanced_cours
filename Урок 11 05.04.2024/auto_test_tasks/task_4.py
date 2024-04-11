class Matrix:
    count = 0
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
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
        line = ''
        for row in self.data:
            row = [str(i) for i in row]
            line += ' '.join(row) + '\n'
        return line
    
    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols and self.__str__() == other.__str__():
                return True
            else:
                return False
        else:
            raise TypeError('Ошибка класса!')
        
   def __add__(self, other):
       if isinstance(other, Matrix):
           
            if self.rows == other.rows and self.cols == other.cols:
                for i in range(self.rows):
                    for j in range(self.cols):
                                
                
        else:
            raise TypeError('Ошибка класса!')

mx = Matrix(4, 5)
mx2 = Matrix(3, 2)
print(repr(mx))
print(mx == mx2)
