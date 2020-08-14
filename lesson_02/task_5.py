"""
5. Реализовать расчет цены товара со скидкой.

Величина скидки должна передаваться в качестве аргумента в дочерний класс.

Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.

В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой.

Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы
(вторая и третья строка после объявления дочернего класса).
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
    def __init__(self, name, price, discount):
        super().__init__(name, price)

        self.discount = discount

    def __str__(self):
        return f'{self.get_name()} - {self.get_price() * self.discount}'

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()}'


if __name__ == '__main__':
    item_1 = ItemDiscountReport('botle', 200, 0.5)
    assert item_1.get_parent_data() == 'botle - 200'

    item_1.set_name('big botle')
    item_1.set_price(300)

    assert item_1.get_parent_data() == 'big botle - 300'

    assert item_1.__str__() == 'big botle - 150.0'

