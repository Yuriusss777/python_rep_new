# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
import time


class MyStr(str):
    """Пользовательский класс строки с дополнительной информацией об авторе и времени создания."""

    def __new__(cls, value, avtor):
        """
        Создает новый экземпляр MyStr.

        Args:
            value (str): Значение строки.
            avtor (str): Имя автора.

        Returns:
            MyStr: Новый экземпляр MyStr.
        """
        instance = super().__new__(cls, value)
        instance.avtor = avtor
        instance.time = time.time()
        return instance

    def __str__(self):
        """
        Возвращает строковое представление экземпляра.

        Returns:
            str: Строковое представление для пользователя.
        """
        return f"Представление для пользователя: {self.avtor} {self.time}"

    def __repr__(self):
        """
        Возвращает программисту понятное представление экземпляра.

        Returns:
            str: Понятное представление для программиста.
        """
        return f"Представление для программиста: {self.avtor} {self.time}"


a = MyStr('Name', avtor='Bob')

print(repr(a))  # Вывод: Представление для программиста: Bob <временная метка>

print(a)  # Вывод: Представление для пользователя: Bob <временная метка>
