"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = [1, 2, 3, 4, 5]

with open('numbers.txt', 'w', encoding='utf-8') as file:
    file.write(' '.join(map(str, numbers)))

with open('numbers.txt', 'r', encoding='utf-8') as file:
    numbers = file.read().split()
    numbers = list(map(int, numbers))
    sum_of_numbers = sum(numbers)

print(f"Сумма чисел: {sum_of_numbers}")
