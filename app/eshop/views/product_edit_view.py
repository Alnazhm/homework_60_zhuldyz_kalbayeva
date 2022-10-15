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





# def product_edit_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "GET":
#         form = ProductForm(initial={
#             'title': product.title,
#             'description': product.description,
#             'category': product.category,
#             'price': product.price,
#             'balance': product.balance,
#             'images_url': product.images_url
#         })
#         return render(request, 'product_edit.html', context={'form': form, 'product': product})
#     elif request.method == 'POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product.title = form.cleaned_data['title']
#             product.description = form.cleaned_data['description']
#             product.category = form.cleaned_data['category']
#             product.price = form.cleaned_data['price']
#             product.balance = form.cleaned_data['balance']
#             product.images_url = form.cleaned_data['images_url']
#             product.save()
#             return redirect(reverse('product_detail', kwargs={'pk': product.pk}))
#         else:
#             return render(request, 'product_edit.html', context={'form': form, 'product': product})
