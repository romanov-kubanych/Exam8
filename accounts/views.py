from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import MyUserCreationForm, UserUpdateForm

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = 'create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:product_index')
        return next_url


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["projects"] = self.object.projects_user.all()
        return context


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "update_profile.html"
    context_object_name = "user_object"

    def get_success_url(self):
        return reverse("accounts:detail", kwargs={"pk": self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user

