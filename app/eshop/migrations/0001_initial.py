# Generated by Django 4.1.2 on 2022-10-17 21:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('category', models.CharField(choices=[('Electronics', 'Электроника'), ('Kitchen_electronics', 'Кухонная электроника'), ('Cars', 'Машины'), ('Other', 'Разное')], default='Other', max_length=50, verbose_name='Категория')),
                ('images_url', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Ссылка на изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
                ('balance', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Дата удаления')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['category', 'title'],
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('products', models.ManyToManyField(blank=True, related_name='orders', to='eshop.product', verbose_name='Заказы пользователей')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Остаток')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='eshop.userorder', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='eshop.product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_in_basket', to='eshop.product', verbose_name='Статус')),
            ],
        ),
    ]
