from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = "user_app/login.html"

    def get_success_url(self):
        if self.request.user.is_superuser:  # Check if admin
            return reverse('admin:index')
        else:
            return reverse('test_page')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


