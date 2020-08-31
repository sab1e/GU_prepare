from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='название продукта', max_length=128)
    measure_unit = models.CharField(verbose_name='единица измерения',
                                    max_length=128)
    price = models.DecimalField(verbose_name='цена продукта',
                                max_digits=8,
                                decimal_places=2,
                                default=0)
    reciept_date = models.DateTimeField(verbose_name='дата поступления')
    vendor = models.CharField(verbose_name='поставщик', max_length=128)
