"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReportName(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)

        self.discount = discount

    def __str__(self):
        return f'{self.get_name()} - {self.get_price() * self.discount}'

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()}'

    def get_info(self):
        return f'{self.get_name()}'


class ItemDiscountReportPrice(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_info(self):
        return f'{self.get_price()}'


if __name__ == '__main__':
    item_botle = ItemDiscountReportName('botle', 200, 0.5)
    assert item_botle.get_parent_data() == 'botle - 200'

    item_botle.set_name('big botle')
    item_botle.set_price(300)

    assert item_botle.get_parent_data() == 'big botle - 300'

    assert item_botle.__str__() == 'big botle - 150.0'

    item_tin_box = ItemDiscountReportPrice('tin box', 100)

    print(item_botle.get_info())
    print(item_tin_box.get_info())

    for obj in (item_botle, item_tin_box):
        print(obj.get_info())

    def obj_handler(obj):
        print(obj.get_info())

    obj_handler(item_botle)
    obj_handler(item_tin_box)
