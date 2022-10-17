from django.shortcuts import redirect
from django.views.generic import CreateView
from eshop.models import UserOrder
from eshop.models import ProductInBasket
from eshop.models import Product
from eshop.models import ProductOrder
from eshop.forms import OrderForm


class OrderCreateView(CreateView):
    model = UserOrder

    def post(self, request, *args, **kwargs):
        self.order_form = OrderForm(self.request.POST)
        if self.order_form.is_valid():
            products_from_basket = ProductInBasket.objects.all()
            user_order = UserOrder.objects.create(**self.order_form.cleaned_data)
            for products in products_from_basket:
                product = Product.objects.get(id=products.product_id)
                order_product = ProductOrder.objects.create(
                    order=user_order,
                    product=product,
                    count=products.count
                )
        product = ProductInBasket.objects.all()
        product.delete()
        return redirect('products')