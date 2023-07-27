# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self.matrix.append(row)

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += " ".join(str(num) for num in row)
            result += "\n"
        return result

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be added.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns of first matrix must be equal to the number of rows of the second matrix.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result


matrix_a = Matrix(2, 3)
matrix_a.matrix = [[1, 2, 3], [4, 5, 6]]
matrix_b = Matrix(2, 3)
matrix_b.matrix = [[7, 8, 9], [10, 11, 12]]
matrix_c = Matrix(3, 2)
matrix_c.matrix = [[1, 2], [3, 4], [5, 6]]

print(matrix_a)

print(matrix_a == matrix_b)

print(matrix_a + matrix_b)

print(matrix_a * matrix_c)

