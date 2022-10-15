from django.urls import reverse
from eshop.models import Product
from eshop.forms import ProductForm
from django.views.generic import CreateView


class ProductCreate(CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})
