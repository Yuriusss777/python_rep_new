"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

less_than_20k = []
total_salary = 0
employee_count = 0

with open('zp.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a = line.split()
        if len(a) == 2:
            surname = a[0]
            salary = float(a[1])
            total_salary += salary
            employee_count += 1

            if salary < 20000:
                less_than_20k.append(surname)

average_salary = total_salary / employee_count

print("Сотрудники с окладом менее 20 тыс.:")
for surname in less_than_20k:
    print(surname)

print(f"Средний доход сотрудников: {average_salary:.2f}")
