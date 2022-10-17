from eshop.models import ProductInBasket
from django.views.generic import ListView
from eshop.forms import OrderForm

class BasketView(ListView):
    template_name = 'basket.html'
    model = ProductInBasket

    def get(self, request, *args, **kwargs):
        self.order_form = OrderForm(self.request.GET)
        self.order_value = self.get_order_value()
        return super().get(request, *args, **kwargs)

    def get_order_value(self):
        if self.order_form.is_valid():
            return self.order_form.cleaned_data
        return None

    def total(self):
        products_in_basket = ProductInBasket.objects.all()
        total = 0
        for product in products_in_basket:
            total += product.count * product.product.price
        return total

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BasketView, self).get_context_data(object_list=object_list, **kwargs)
        context['total'] = self.total()
        context['order_form'] = self.order_form
        context['products_in_basket'] = ProductInBasket.objects.all()
        return context






