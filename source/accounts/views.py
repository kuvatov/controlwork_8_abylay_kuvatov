from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        reviews = user.comments.all()
        context['reviews'] = reviews
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'profile/profile_update.html'

    def get_success_url(self):
        return reverse_lazy('profile_detail', args=(self.object.id,))


class ProfilePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profile/profile_password_change.html'
    success_url = reverse_lazy('product_list')
