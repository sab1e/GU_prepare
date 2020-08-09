"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)
"""
import random


# функция генератор
def random_number_generator(min_value, max_value, length_value):
    while length_value > 0:
        yield random.randint(min_value, max_value)
        length_value -= 1


# функция, возвращающая выражение-генератор
def random_generator_expression(min_value, max_value, length_value):
    return (random.randint(min_value, max_value)
            for _ in range(length_value))


random_values = random_number_generator(-10, 10, 10)

random_values_list = []
random_values_dict = {}
for value in random_values:
    if value != 0:
        random_values_list.append(value)
        random_values_dict['elem_' + str(value)] = value

print(random_values_list)
print(random_values_dict)

random_values_expression = random_generator_expression(-1, 1, 10)

random_values_list_expression = [value for value in random_values_expression
                                 if value != 0]
random_values_dict_expression = {'elem_' + str(value): value
                                 for value in random_values_list_expression}

print(random_values_list_expression)
print(random_values_dict_expression)