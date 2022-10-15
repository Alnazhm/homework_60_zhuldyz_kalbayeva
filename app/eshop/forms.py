from django import forms
from eshop.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'images_url', 'price', 'balance')

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')