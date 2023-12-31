"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asphalt_mass(self, mass_per_meter, thickness):
        asphalt_mass = self._length * self._width * mass_per_meter * thickness
        return asphalt_mass


road = Road(20, 5000)
asphalt_mass = road.calculate_asphalt_mass(25, 0.05)
print(f"Масса асфальта: {asphalt_mass} кг")
