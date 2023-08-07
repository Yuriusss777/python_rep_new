import os
import logging
from collections import namedtuple

# Создание объекта namedtuple для хранения информации о файле/каталоге
FileEntry = namedtuple('FileEntry', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_directory_content(directory_path):
    """Получает информацию о содержимом указанной директории"""
    directory_content = []
    for entry in os.scandir(directory_path):
        if entry.is_file():
            name, extension = os.path.splitext(entry.name)
            entry_info = FileEntry(name=name, extension=extension, is_directory=False,
                                   parent_directory=os.path.basename(directory_path))
        elif entry.is_dir():
            entry_info = FileEntry(name=entry.name, extension='', is_directory=True,
                                   parent_directory=os.path.basename(directory_path))
        directory_content.append(entry_info)
    return directory_content


def save_to_file(data, file_path):
    """Сохраняет информацию о содержимом директории в текстовый файл"""
    with open(file_path, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(f"Name: {entry.name}\n")
            file.write(f"Extension: {entry.extension}\n")
            file.write(f"Is Directory: {entry.is_directory}\n")
            file.write(f"Parent Directory: {entry.parent_directory}\n")
            file.write("\n")


def main():
    """Установка конфигурации логирования"""
    logging.basicConfig(filename='log.txt', level=logging.INFO)

    directory_path = input("Введите путь до директории: ")
    directory_content = get_directory_content(directory_path)

    try:
        save_to_file(directory_content, 'output.txt')
        logging.info('Данные успешно сохранены в файл.')
    except Exception as e:
        logging.error(f'При сохранении данных произошла ошибка: {str(e)}')


if __name__ == '__main__':
    main()
