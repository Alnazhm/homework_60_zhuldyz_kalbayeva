from django.contrib import admin
from eshop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'price', 'balance', 'images_url', 'created_at', 'changed_at')
    list_filter = ('id', 'title', 'description', 'category', 'price', 'balance', 'images_url', 'created_at', 'changed_at')
    search_fields = ('title', 'description', 'category', 'price', 'balance')
    fields = ('title', 'description', 'category', 'price', 'balance')

admin.site.register(Product, ProductAdmin)
