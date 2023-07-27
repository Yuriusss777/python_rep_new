import time


class MyStr(str):
    def new(cls, value, avtor):
        """ Создает новый экземпляр класса MyStr с указанным значением и автором и возвращает его."""
        instance = super().new(cls, value)
        instance.avtor = avtor
        instance.time = time.time()
        return instance

    def str(self):
        """Возвращает строковое представление экземпляра класса MyStr."""
        return super().str() + f" (автор: {self.avtor})"

    def repr(self):
        """Возвращает представление экземпляра класса MyStr для вывода на печать."""
        return self.str()


a = MyStr('Name', avtor='Bob')

print(a.upper())

print(a.time)


class Matrix:
    def init(self, elements):
        """ Создает новый экземпляр класса Matrix с указанными элементами."""
        self.elements = elements

    def eq(self, other):
        """ Проверяет равенство текущей матрицы с другой матрицей"""
        if isinstance(other, Matrix):
            return self.elements == other.elements
        return False

    def add(self, other):
        """ Выполняет сложение текущей матрицы с другой матрицей"""
        if isinstance(other, Matrix) and len(self.elements) == len(other.elements) and \
                len(self.elements[0]) == len(other.elements[0]):
            result = []
            for i in range(len(self.elements)):
                row = []
                for j in range(len(self.elements[0])):
                    row.append(self.elements[i][j] + other.elements[i][j])
                result.append(row)
            return Matrix(result)
        raise ValueError("Матрицы имеют неподходящие размеры для сложения.")

    def mul(self, other):
        """ Выполняет умножение текущей матрицы на другую матрицу или скаляр."""
        if isinstance(other, Matrix):
            if len(self.elements[0]) != len(other.elements):
                raise ValueError("Матрицы имеют неподходящие размеры для умножения.")
            result = []
            for i in range(len(self.elements)):
                row = []
                for j in range(len(other.elements[0])):
                    element = sum(self.elements[i][k] * other.elements[k][j] for k in range(len(self.elements[i])))
                    row.append(element)
                result.append(row)
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = []
            for i in range(len(self.elements)):
                row = []
                for j in range(len(self.elements[0])):
                    row.append(self.elements[i][j] * other)
                result.append(row)
            return Matrix(result)
        else:
            raise TypeError("Умножение доступно только для матрицы")

    def __add__(self, other):
        return self.add(other)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

m3 = m1 + m2

for row in m3.elements:
    print(row)

# После исправлений код будет выводить результат сложения матрицы:
#
# [10, 10, 10]
# [10, 10, 10]
# [10, 10, 10]