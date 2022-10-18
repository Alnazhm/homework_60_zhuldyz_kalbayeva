from eshop.models import Product
from django.views.generic import ListView
from urllib.parse import urlencode
from eshop.forms import SearchForm
from django.db.models import Q
from eshop.forms import AddProductToBasketForm
from eshop.models import ProductInBasket


class IndexView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-category', 'title')
    paginate_by = 5
    paginate_orphans = 0
    error_text = None
    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.product_add_basket_form = AddProductToBasketForm(self.request.GET)
        self.product_add_basket_value = self.get_product_in_basket()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_product_in_basket(self):
        if self.product_add_basket_form.is_valid():
            return self.product_add_basket_form.cleaned_data.get('count')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True, balance__lt=1)
        if self.search_value:
            query = Q(title__icontains=self.search_value)
            print(query.__dict__)
            queryset = queryset.filter(query)
        if self.product_add_basket_value:
            product_id = self.kwargs.get('pk')
            count = self.product_add_basket_value
            product = Product.objects.get(id=product_id)
            if product.balance >= count:
                if ProductInBasket.objects.filter(product=product).exists():
                    product_in_basket = ProductInBasket.objects.get(product_id=product_id)
                    sum_of_count = product_in_basket.count + count
                    ProductInBasket.objects.filter(product_id=product_id).update(count=sum_of_count)
                else:
                    ProductInBasket.objects.create(product_id=product_id, count=count)
            else:
                self.error_text = 'Вы ввели слишком большое количество чем на складе'
                return queryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['product_add_basket_form'] = self.product_add_basket_form
        context['error_text'] = self.error_text
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
