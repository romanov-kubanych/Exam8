from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/create.html'
    permission_required = 'webapp.add_task'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('webapp:product_view', pk=product.pk)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reviews/update.html'
    form_class = ReviewForm
    permission_required = 'webapp.change_review'

    def has_permission(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == review.author

    def form_valid(self, form):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        form = form.save(commit=False)
        form.status = False
        form.save()
        return redirect('webapp:product_view', pk=review.product.pk)


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/delete.html"
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == review.author

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.id})

