from django.db import models


class ProductInBasket(models.Model):
    product = models.ForeignKey(
        to='eshop.Product',
        verbose_name='Статус',
        related_name='products_in_basket',
        on_delete=models.CASCADE
    )
    count = models.IntegerField(
        verbose_name='Количество'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def str(self):
        return f'{self.product} {self.count}'
