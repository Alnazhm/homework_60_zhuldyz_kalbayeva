from django.urls import reverse
from eshop.models import Product
from eshop.forms import ProductForm
from django.views.generic import UpdateView


class ProductUpdateView(UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

