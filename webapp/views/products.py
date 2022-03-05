from django.views.generic import ListView, DetailView

from webapp.models import Product


class ProductIndex(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'


class ProductView(DetailView):
    model = Product
    template_name = 'products/view.html'
