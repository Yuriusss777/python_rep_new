import doctest


class Rectangle:
    """Создает экземпляр прямоугольника с заданными длиной и шириной """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Вычисляет площадь прямоугольника"""
        return self.length * self.width

    def perimeter(self):
        """Вычисляет периметр прямоугольника"""
        return 2 * (self.length + self.width)


def test_rectangle_area():
    """
    >>> rectangle = Rectangle(4,5)
    >>> rectangle.area()
    20

    >>> rectangle = Rectangle(3, 7)
    >>> rectangle.area()
    21
    """



def test_rectangle_perimeter():
    """
    >>> rectangle = Rectangle(4, 5)
    >>> rectangle.perimeter()
    18

    >>> rectangle = Rectangle(3, 7)
    >>> rectangle.perimeter()
    20
    """



if __name__ == "__main__":
    doctest.testmod()
