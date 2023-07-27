# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def area(self):
        return self.width * self.lenght

    def perimetr(self):
        return 2 * (self.width + self.lenght)

    def __add__(self, other):
        summary_perimetr = self.perimetr() + other.perimetr()
        width_rectangle_c = self.width
        length_rectangle_c = summary_perimetr / 2 - width_rectangle_c

        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __sub__(self, other):
        sub_perimetr = abs(self.perimetr() - other.perimetr())
        width_rectangle_c = min(self.width, other.width, self.lenght, other.lenght)
        length_rectangle_c = sub_perimetr / 2 - width_rectangle_c

        return Rectangle(width_rectangle_c, length_rectangle_c)

rectangle_a = Rectangle(2, 3)
rectangle_b = Rectangle(5, 10)

print(rectangle_a.perimetr())
print(rectangle_b.perimetr())

rectangle_c = rectangle_a + rectangle_b
print(rectangle_c.perimetr(), rectangle_c.width, rectangle_c.lenght)
