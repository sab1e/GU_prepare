"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""
import os
import re


def create_file(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.isfile(file_path):
        print('файл существует')
        return
    else:
        return open(file_path, 'w', encoding='UTF-8')


def open_file(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    return open(file_path, 'r', encoding='UTF-8')


def scan_file(file):
    text = file.read()
    pattern = r'\d*\s(\w*)\n'
    words = re.findall(pattern, text)

    return words


file = open_file('task4.txt')
words = scan_file(file)

new_data = list(zip(words, words))
new_file = create_file('task5.txt')

for el in words:
    new_file.write(f'{el} {el}\n')
