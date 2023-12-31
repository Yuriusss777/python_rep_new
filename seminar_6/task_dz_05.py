"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Используем ручку {self.title} для рисования.")


class Pencil(Stationery):
    def draw(self):
        print(f"Используем карандаш {self.title} для рисования.")


class Handle(Stationery):
    def draw(self):
        print(f"Используем маркер {self.title} для рисования.")


stationery = Stationery("Канцелярская принадлежность")
stationery.draw()

pen = Pen("синяя")
pen.draw()

pencil = Pencil("ТМ")
pencil.draw()

handle = Handle("желтый")
handle.draw()
