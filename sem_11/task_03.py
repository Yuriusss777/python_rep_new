# Добавьте к задачам 1 и 2 строки документации для классов.

# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

import time


class MyStr(str):
    def __new__(cls, vaulue, avtor):
        instance = super().__new__(cls, vaulue)
        instance.avtor = avtor
        instance.time = time.time()
        return instance

    def __str__(self):
        return f"Представление для пользователя {self.avtor} {self.time}"

    def __repr__(self):
        return f"Представление для программиста {self.avtor} {self.time}"


a = MyStr('Name', avtor='Bob')

print(repr(a))

print(a)
