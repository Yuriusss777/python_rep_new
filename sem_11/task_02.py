# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


class Archive:
    list_archive = []

    def __init__(self, number, string):
        self.number = number
        self.string = string
        self.list_archive.append({"number": self.number, "string": self.string})

    def __str__(self):
        return f"Number: {self.number}, String: {self.string}"

    @classmethod
    def get_list_archive(cls):
        return cls.list_archive
