"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

number_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('my_text.txt', 'r', encoding='utf-8') as f_1, \
        open('my_text2.txt', 'w', encoding='utf-8') as f_2:
    for line in f_1:
        a = line.split(' — ')

        if len(a) == 2:
            if a[0] in number_dict:
                russian_number = number_dict[a[0]]
                f_2.write(f"{russian_number} — {a[1]}\n")
            else:
                f_2.write(line)
        else:
            f_2.write(line)
