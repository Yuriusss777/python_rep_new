"""Превратите функции в методы класса. Задачи должны решаться через вызов методов экземпляра.
Например:
1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним."""


class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def check_triangle_existence(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False

    def get_triangle_type(self):
        if self.a == self.b == self.c:
            return "равносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "равнобедренный"
        else:
            return "разносторонний"


a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

triangle = Triangle()
triangle.a = a
triangle.b = b
triangle.c = c

if triangle.check_triangle_existence():
    print("Треугольник с такими сторонами существует.")
    triangle_type = triangle.get_triangle_type()
    print("Треугольник является", triangle_type)
else:
    print("Треугольник с такими сторонами не существует.")
