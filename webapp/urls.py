from django.urls import path

from views.products import ProductIndex, ProductView

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndex.as_view(), name='product_index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
]