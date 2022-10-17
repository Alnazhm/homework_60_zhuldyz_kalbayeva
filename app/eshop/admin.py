from django.contrib import admin
from eshop.models import Product
from eshop.models import ProductInBasket
from eshop.models import UserOrder
from eshop.models import ProductOrder


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'price', 'balance', 'images_url', 'created_at', 'changed_at')
    list_filter = ('id', 'title', 'description', 'category', 'price', 'balance', 'images_url', 'created_at', 'changed_at')
    search_fields = ('title', 'description', 'category', 'price', 'balance')
    fields = ('title', 'description', 'category', 'price', 'balance')


admin.site.register(Product, ProductAdmin)

class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'product_id', 'created_at', 'updated_at')
    list_filter = ('id', 'count', 'product_id', 'created_at', 'updated_at')
    search_fields = ('count', 'product_id', 'created_at', 'updated_at')
    fields = ('count', 'product_id', 'created_at', 'updated_at')
    readonly_fields = ['id', 'created_at', 'updated_at']

admin.site.register(ProductInBasket, ProductInBasketAdmin)

class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'phone', 'address', 'created_at', 'updated_at')
    list_filter = ('id', 'user_name', 'phone', 'address', 'created_at', 'updated_at')
    search_fields = ('id', 'user_name', 'phone', 'address', 'created_at', 'updated_at')
    fields = ('user_name', 'phone', 'address')
    readonly_fields = ['id', 'created_at', 'updated_at']

admin.site.register(UserOrder, UserOrderAdmin)

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'order_id', 'product_id', 'created_at')
    list_filter = ('id', 'count', 'order_id', 'product_id', 'created_at')
    search_fields = ('id', 'count', 'order_id', 'product_id', 'created_at')
    fields = ('id', 'count', 'order_id', 'product_id')
    readonly_fields = ['id', 'created_at', 'updated_at']

admin.site.register(ProductOrder, ProductOrderAdmin)