from django.db import models


class Currency(models.Model):
    currency_type = models.CharField(verbose_name='Payment currency', max_length=5, unique=True, null=False, blank=False)

    def __str__(self):
        return self.currency_type


class Item(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=100, null=False, blank=False)
    description = models.CharField(verbose_name='Product description', max_length=500)
    price = models.FloatField(verbose_name='Price', null=False, blank=False)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT,
                                 help_text="Select currency",
                                 verbose_name="Pyment currency", null=False, blank=False)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(verbose_name='Discount name', max_length=100, null=False, blank=False)
    discount = models.FloatField(verbose_name='Discount', blank=True, null=True)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(verbose_name='Tax name', max_length=100, blank=False, null=False)
    tax_size = models.FloatField(verbose_name='Tax size', blank=False, null=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ManyToManyField(Item, blank=False, verbose_name='Order')
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT, verbose_name='Discount', blank=True, null=True)
    tax = models.ForeignKey(Tax, on_delete=models.PROTECT, verbose_name='Tax size', blank=False, null=False)
    order_price = models.FloatField(verbose_name='Order price', blank=False, null=False)

    def __str__(self):
        return str(self.id)


# Модель Order, в которой можно объединить несколько Item и
# сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
# Модели Discount, Tax, которые можно прикрепить к модели Order и связать
# с соответствующими атрибутами при создании платежа в Stripe - в таком случае
# они корректно отображаются в Stripe Checkout форме.
