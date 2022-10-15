from django.shortcuts import render
from eshop.models import Product



def products_view(request):
    products = Product.objects.filter(is_deleted=False, balance__gte=1)

    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)