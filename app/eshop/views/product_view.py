from eshop.models import Product
from django.views.generic import DetailView


# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'product.html', context={'product': product})

class ProductView(DetailView):
    template_name = 'product.html'
    model = Product