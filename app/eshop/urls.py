from eshop.views.products_view import products_view
from eshop.views.product_view import product_detail_view
from eshop.views.product_add_view import product_add_view
from eshop.views.product_edit_view import product_edit_view
from eshop.views.product_delete_view import product_delete_view, confirm_delete_product_view
from django.urls import path

urlpatterns = [
    path('', products_view, name='products'),
    path('products/<int:pk>', product_detail_view, name='product_detail'),
    path('products/add/', product_add_view, name='product_add'),
    path('products/<int:pk>/delete', product_delete_view, name="product_delete"),
    path('products/<int:pk>/edit', product_edit_view, name="product_edit"),
    path('tasks/deleted/<int:pk>', confirm_delete_product_view, name='confirm_delete')
]