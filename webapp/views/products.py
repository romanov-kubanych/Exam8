from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductIndex(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'


class ProductView(DetailView):
    model = Product
    template_name = 'products/view.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/delete.html"

    def get_success_url(self):
        return reverse('webapp:product_index')
