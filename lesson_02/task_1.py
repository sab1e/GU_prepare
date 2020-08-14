"""
Проверить механизм наследования в Python.

Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену.

Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую
за отображение информации о товаре в одной строке.

Проверить работу программы.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_parent_data(self):
        return f'{self.name} - {self.price}'


if __name__ == '__main__':
    item_1 = ItemDiscountReport('botle', 200)
    assert item_1.get_parent_data() == 'botle - 200'

