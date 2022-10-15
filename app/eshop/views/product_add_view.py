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


# def product_add_view(request):
#     form = ProductForm()
#     if request.method == 'GET':
#         context = {'form': form}
#         return render(request, 'add_product.html', context)
#     form = ProductForm(request.POST)
#     if not form.is_valid():
#         context = {
#             'form': form
#         }
#         return render(request, 'add_product.html', context)
#     product = Product.objects.create(**form.cleaned_data)
#     return redirect(reverse('product_detail', kwargs={'pk': product.pk}))