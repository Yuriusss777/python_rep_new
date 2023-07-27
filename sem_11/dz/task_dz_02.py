# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.

class Archive:
    list_archive = []

    def __init__(self, number, string):
        """Создает новый объект класса Archive и добавляет его в list_archive."""
        self.number = number
        self.string = string
        self.list_archive.append({"number": self.number, "string": self.string})

    def __str__(self):
        """Возвращает строковое представление объекта класса Archive."""

        return f"Number: {self.number}, String: {self.string}"

    @classmethod
    def get_list_archive(cls):
        """Возвращает list_archive - список архивных записей."""

        return cls.list_archive

# Создание объектов класса Archive
a1 = Archive(1, 'string1')
a2 = Archive(2, 'string2')

# Вывод информации на печать
print(a1)
print(a2)

# Получение списка архивных записей
archive_list = Archive.get_list_archive()
print(archive_list)


