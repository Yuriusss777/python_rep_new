# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)


import time


class MyStr(str):
    def __new__(cls, value, avtor):
        instance = super().__new__(cls, value)
        instance.avtor = avtor
        instance.time = time.time()
        return instance


a = MyStr('Name', avtor='Bob')

print(a.upper())

print(a.time)
