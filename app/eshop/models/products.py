from django.db import models
from django.db.models import TextChoices
from django.core.validators import MinValueValidator
from django.utils import timezone


class CategoryChoices(TextChoices):
    ELECTRONICS = 'Electronics', 'Электроника'
    KITCHEN_ELECTRONICS = 'Kitchen_electronics', 'Кухонная электроника'
    CARS = 'Cars', 'Машины'
    OTHER = 'Other', 'Разное'


class Product(models.Model):
    title = models.CharField(verbose_name='Наименование товара', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name="Описание", max_length=2000, null=True, blank=True)
    category = models.CharField(verbose_name="Категория", choices=CategoryChoices.choices, default=CategoryChoices.OTHER, max_length=50, null=False, blank=False)
    images_url = models.TextField(verbose_name="Ссылка на изображение", max_length=3000, null=True, blank=True)
    price = models.DecimalField(verbose_name="Стоимость", max_digits=7, decimal_places=2)
    balance = models.IntegerField(verbose_name="Остаток", validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.category} - {self.price} - {self.balance}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'title']


    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()