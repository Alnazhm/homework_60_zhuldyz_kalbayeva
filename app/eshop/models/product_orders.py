from django.db import models


class ProductOrder(models.Model):
    order = models.ForeignKey(
        to='eshop.UserOrder',
        verbose_name='Заказ',
        related_name='order',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='eshop.Product',
        verbose_name='Товар',
        related_name='product',
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