# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __it__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


rectangle_a = Rectangle(2, 3)
rectangle_b = Rectangle(5, 10)

print(rectangle_a > rectangle_b)
