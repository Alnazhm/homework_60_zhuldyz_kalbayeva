from eshop.views.products_view import IndexView
from eshop.views.product_view import ProductView
from eshop.views.product_add_view import ProductCreate
from eshop.views.product_edit_view import ProductUpdateView
from eshop.views.product_delete_view import ProductDeleteView
from eshop.views.basket_view import BasketView
from eshop.views.create_order_view import OrderCreateView
from eshop.views.delete_from_basket_view import ProductInBasketDeleteView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='products'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductCreate.as_view(), name='product_add'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name="product_edit"),
    path('tasks/deleted/<int:pk>', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/<int:pk>/product_add_basket', IndexView.as_view(), name='products'),
    path('products/inbasket', BasketView.as_view(), name='products_in_basket'),
    path('products/inbasket/create_order', OrderCreateView.as_view(), name='create_order'),
    path('products/inbasket/<int:pk>/delete_order', ProductInBasketDeleteView.as_view(), name='delete_order')

]