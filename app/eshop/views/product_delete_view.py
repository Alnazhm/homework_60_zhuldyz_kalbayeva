from eshop.models import Product
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class ProductDeleteView(DeleteView):
    template_name = 'delete_confirm_page.html'
    model = Product
    success_url = reverse_lazy('products')

