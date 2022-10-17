from django import forms
from eshop.models import Product
from eshop.models import ProductInBasket
from eshop.models import UserOrder


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'images_url', 'price', 'balance')

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class AddProductToBasketForm(forms.ModelForm):
    count = forms.IntegerField(required=True)
    class Meta:
        model = ProductInBasket
        fields = ('count',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = ('user_name', 'phone', 'address')