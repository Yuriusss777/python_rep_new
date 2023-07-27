import time


class MyStr(str):
    def __new__(cls, value, avtor):
        """ Создает новый экземпляр класса MyStr с указанным значением и автором и возвращает его."""
        instance = super().__new__(cls, value)
        instance.avtor = avtor
        instance.time = time.time()
        return instance

    def __str__(self):
        """Возвращает строковое представление экземпляра класса MyStr."""
        return super().__str__() + f" (автор: {self.avtor})"

    def __repr__(self):
        """Возвращает представление экземпляра класса MyStr для вывода на печать."""
        return self.__str__()

    def upper(self):
        """Возвращает версию строки в верхнем регистре."""
        return MyStr(super().upper(), avtor=self.avtor)


a = MyStr('Name', avtor='Bob')

print(a.upper())

print(a.time)

print(a.__str__())
print(a.__repr__())

