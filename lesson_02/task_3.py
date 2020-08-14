"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_parent_data(self):
        return f'{self.get_name()} - {self.get_price()}'


if __name__ == '__main__':
    item_1 = ItemDiscountReport('botle', 200)
    assert item_1.get_parent_data() == 'botle - 200'
