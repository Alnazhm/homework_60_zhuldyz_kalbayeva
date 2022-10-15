from eshop.models import Product
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class ProductDeleteView(DeleteView):
    template_name = 'delete_confirm_page.html'
    model = Product
    success_url = reverse_lazy('products')

# def product_delete_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'delete_confirm_page.html', context={'product': product})
#
# def confirm_delete_product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     return redirect('products')