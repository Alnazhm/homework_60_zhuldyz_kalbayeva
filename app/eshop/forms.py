from django import forms
from django.forms import widgets
from eshop.models import Product

class ProductForm(forms.ModelForm):
    # title = forms.CharField(max_length=100, required=True, label='Наименование товара',
    #                             widget=forms.TextInput({'class': 'form-input'}))
    # description = forms.CharField(max_length=2000, required=False, label='Описание',
    #                                    widget=widgets.Textarea)
    # category = forms.ChoiceField(choices=CategoryChoices.choices, label='Категория')
    # images_url = forms.CharField(max_length=3000, required=False,  label='Ссылка на изображение')
    # price = forms.DecimalField(max_digits=7, decimal_places=2, label='Стоимость')
    # balance = forms.IntegerField(min_value=0, label='Остаток')

    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'images_url', 'price', 'balance')

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')