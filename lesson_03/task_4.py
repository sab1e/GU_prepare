"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан
в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""

import os
import string
import random

START_NUM = 0
END_NUM = 100
LENGTH_OF_WORD = 10


def create_file(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.isfile(file_path):
        print('файл существует')
        return
    else:
        return open(file_path, 'w', encoding='UTF-8')


def generate_numeric(quantity):
    return [random.randint(START_NUM, END_NUM) for _ in range(quantity)]


def generate_alpha(quantity):
    text_list = []
    for _ in range(quantity):
        random_word = ''.join(
            [string.ascii_lowercase[
                 random.randint(0, len(string.ascii_lowercase) - 1)]
             for _ in range(LENGTH_OF_WORD)])
        text_list.append(random_word)
    return text_list


file = create_file('task4.txt')
if file:
    num = generate_numeric(5)
    alpha = generate_alpha(5)
    concat = list(zip(num, alpha))

    for el in concat:
        file.write(f'{el[0]} {el[1]}\n\n')

    file.close()
