from django.shortcuts import render, redirect, get_object_or_404
from eshop.models import Product


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'delete_confirm_page.html', context={'product': product})

def confirm_delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')