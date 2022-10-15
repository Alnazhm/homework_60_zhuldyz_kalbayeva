from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from eshop.models import Product
from eshop.forms import ProductForm

def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            'title': product.title,
            'description': product.description,
            'category': product.category,
            'price': product.price,
            'balance': product.balance,
            'images_url': product.images_url
        })
        return render(request, 'product_edit.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.balance = form.cleaned_data['balance']
            product.images_url = form.cleaned_data['images_url']
            product.save()
            return redirect(reverse('product_detail', kwargs={'pk': product.pk}))
        else:
            return render(request, 'product_edit.html', context={'form': form, 'product': product})
