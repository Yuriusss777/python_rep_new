"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_lines_and_words(filename):
    line_count = 0
    word_counts = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count = len(words)
            word_counts.append(word_count)

    return line_count, word_counts


filename = 'tavreli.txt'

line_count, word_counts = count_lines_and_words(filename)

print(f"Количество строк: {line_count}")
print("Количество слов в каждой строке:")

for i, count in enumerate(word_counts, 1):
    print(f"Строка {i}: {count}")
