"""
4. Реализовать возможность переустановки значения цены товара.

Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция,
отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()}'


if __name__ == '__main__':
    item_1 = ItemDiscountReport('botle', 200)
    assert item_1.get_parent_data() == 'botle - 200'

    item_1.set_name('big botle')
    item_1.set_price(300)

    assert item_1.get_parent_data() == 'big botle - 300'
