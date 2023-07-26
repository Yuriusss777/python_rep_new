# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import math
import json
import random


def find_roots(a, b, c):
    """Функция для нахождения корней квадратного уравнения"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return None


def generate_csv(filename, rows):
    """Функция для генерации CSV - файла с тремя случайными числами в каждой строке"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


def quadratic_solver_decorator(func):
    """Декоратор для запуска функции нахождения корней квадратного уравнения
    с каждой тройкой чисел из CSV - файла"""

    def wrapper(filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Корнем уравнения: {a}x^2 + {b}x + {c} является: {result}")

    return wrapper


@quadratic_solver_decorator
def find_roots_from_csv(a, b, c):
    return find_roots(a, b, c)


def save_to_json_decorator(func):
    """Декоратор для сохранения переданных параметров и результатов работы функции в JSON - файл"""

    def wrapper(*args):
        result = func(*args)
        if result is not None:
            with open('output.json', 'a', encoding='utf-8') as jsonfile:
                json_data = {'parameters': args, 'result': result}
                json.dump(json_data, jsonfile)
                jsonfile.write('\n')

    return wrapper


@save_to_json_decorator
def find_roots_and_save(a, b, c):
    return find_roots(a, b, c)


# Пример использования функций:

# Нахождение корней квадратного уравнения
roots = find_roots(1, -5, 6)
print(roots)

# Генерация csv файла с тремя случайными числами в каждой строке
generate_csv('data.csv', 100)

# Запуск функции нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
find_roots_from_csv('data.csv')

# Сохранение параметров и результатов работы функции в json файл
find_roots_and_save(1, -5, 6)
