from django.views.generic import CreateView
from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class UserLoginView(LoginView):
    template_name = "user_app/login.html"

    def get_success_url(self):
        if self.request.user.is_superuser:  # Check if admin
            return reverse('admin:index')
        else:
            return reverse('test_page')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('test_page')


class SignUpView(CreateView):
    template_name = "user_app/form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('test_page')
