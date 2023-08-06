import pytest


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


@pytest.fixture
def rectangle():
    return Rectangle(4, 5)


def test_rectangle_area(rectangle):
    assert rectangle.area() == 20


def test_rectangle_perimeter(rectangle):
    assert rectangle.perimeter() == 18


if __name__ == "__main__":
    pytest.main()
