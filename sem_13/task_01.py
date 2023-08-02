# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

class InvalidFactorialRangeError(Exception):
    """определение пользовательского исключения"""

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __str__(self):
        return f"Недопустимый диапазон факториалов: start={self.start}, stop={self.stop}, step={self.step}"


class FactorialGenerator:
    """Класс, который выступает в роли генератора факториалов"""

    def __init__(self, stop: int, start: int = 1, step: int = 1):
        if start < 1 or stop < 1 or step < 1:
            raise InvalidFactorialRangeError(start, stop, step)
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        result = self.calc_fact(self.current)
        self.current += self.step
        return result

    @staticmethod
    def calc_fact(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res


try:
    factorial = FactorialGenerator(-5)
    for i in factorial:
        print(i)
except InvalidFactorialRangeError as e:
    print(e)
