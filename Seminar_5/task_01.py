"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("my_file.txt", "w", encoding='utf-8') as f:
    f.write('String \nstring \nstring \n')
