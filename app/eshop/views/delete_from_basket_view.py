from django.shortcuts import redirect
from django.views.generic import DeleteView
from eshop.models import ProductInBasket



class ProductInBasketDeleteView(DeleteView):
    model = ProductInBasket

    def post(self, request, *args, **kwargs):
        product = ProductInBasket.objects.filter(pk=kwargs['pk'])
        product.delete()
        return redirect('products_in_basket')