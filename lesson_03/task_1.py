"""
1. Написать программу, которая будет содержать функцию
для получения имени файла из полного пути до него.

При вызове функции в качестве аргумента должен передаваться путь до файла.
В функции необходимо реализовать «выделение» из этого пути имени файла (без расширения).

Пример:
функция принмает следующую строку - '../mainapp/views.py'

Результат:
views
"""
import re


def get_file_name(file_path):
    pattern_file_name = r'.*\/(.*)\..*'
    file_name_without_extension = re.findall(pattern_file_name, file_path)
    return file_name_without_extension[0]


if __name__ == '__main__':
    file_name_without_extension = get_file_name('../mainapp/views.py')
    print(file_name_without_extension)
    assert file_name_without_extension == 'views'
