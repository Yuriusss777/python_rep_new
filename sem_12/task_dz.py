# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам
# всех предметов вместе взятых.

import csv


class NameValidator:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value[0].isupper():
            raise ValueError("ФИО должно начинаться с заглавной буквы")
        if not value.replace(" ", "").isalpha():
            raise ValueError("ФИО может содержать только буквы и пробелы")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Student:
    fio = NameValidator()

    def __init__(self, fio, subjects_csv):
        self.fio = fio
        self.subjects = self.load_subjects(subjects_csv)

    def load_subjects(self, subjects_csv):
        subjects = []
        with open(subjects_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                subjects.append(row[0])
        return subjects

    def add_marks(self, subject, marks):
        if subject in self.subjects:
            setattr(self, subject, marks)
        else:
            raise ValueError("Недопустимый предмет")

    def add_test_results(self, subject, results):
        if subject in self.subjects:
            setattr(self, subject + "_test_results", results)
        else:
            raise ValueError("Недопустимый предмет")

    def get_average_marks(self, subject):
        if subject in self.subjects:
            marks = getattr(self, subject, None)
            if marks:
                return sum(marks) / len(marks)
            else:
                return 0.0
        else:
            raise ValueError("Недопустимый предмет")

    def get_average_marks_overall(self):
        total_marks = []
        for subject in self.subjects:
            marks = getattr(self, subject, None)
            if marks:
                total_marks.extend(marks)
        if total_marks:
            return sum(total_marks) / len(total_marks)
        else:
            return 0.0


student = Student("Иванов Иван Иванович", "subjects.csv")
print(student.subjects)

student.add_marks("Математика", [4, 5, 3])
print(student.get_average_marks("Математика"))

student.add_test_results("Физика", [75, 80, 90])
print(student.get_average_marks("Физика"))

student.add_marks("История", [3, 4])
student.add_test_results("История", [95, 85])
print(student.get_average_marks_overall())