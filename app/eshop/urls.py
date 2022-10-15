from eshop.views.products_view import IndexView
from eshop.views.product_view import ProductView
from eshop.views.product_add_view import ProductCreate
from eshop.views.product_edit_view import ProductUpdateView
from eshop.views.product_delete_view import ProductDeleteView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='products'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductCreate.as_view(), name='product_add'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name="product_edit"),
    path('tasks/deleted/<int:pk>', ProductDeleteView.as_view(), name='confirm_delete')
]