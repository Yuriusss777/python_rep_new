# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
class Rectangle:
    """Класс, представляющий прямоугольник."""

    def __init__(self, width, length):
        """
        Инициализирует экземпляр прямоугольника.

        Args:
            width (int): Ширина прямоугольника.
            length (int): Длина прямоугольника.
        """
        self.width = width
        self.length = length

    def area(self):
        """Вычисляет площадь прямоугольника.

        Returns:
            int: Площадь прямоугольника.
        """
        return self.width * self.length

    def perimeter(self):
        """Вычисляет периметр прямоугольника.

        Returns:
            int: Периметр прямоугольника.
        """
        return 2 * (self.width + self.length)

    def __add__(self, other):
        """Выполняет операцию сложения двух прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            Rectangle: Новый прямоугольник, являющийся суммой двух прямоугольников.
        """
        summary_perimeter = self.perimeter() + other.perimeter()
        width_rectangle_c = self.width
        length_rectangle_c = summary_perimeter / 2 - width_rectangle_c

        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __sub__(self, other):
        """Выполняет операцию вычитания двух прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            Rectangle: Новый прямоугольник, являющийся разностью двух прямоугольников.
        """
        sub_perimeter = abs(self.perimeter() - other.perimeter())
        width_rectangle_c = min(self.width, other.width, self.length, other.length)
        length_rectangle_c = sub_perimeter / 2 - width_rectangle_c

        return Rectangle(width_rectangle_c, length_rectangle_c)


rectangle_a = Rectangle(2, 3)
rectangle_b = Rectangle(5, 10)

print(rectangle_a.perimeter())  # Вывод: 10
print(rectangle_b.perimeter())  # Вывод: 30

rectangle_c = rectangle_a + rectangle_b
print(rectangle_c.perimeter(), rectangle_c.width, rectangle_c.length)  # Вывод: 60 2 28
