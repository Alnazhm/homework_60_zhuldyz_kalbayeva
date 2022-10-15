from eshop.models import Product
from django.views.generic import DetailView

class ProductView(DetailView):
    template_name = 'product.html'
    model = Product