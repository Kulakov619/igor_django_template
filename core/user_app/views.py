from django.shortcuts import render
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = "user_app/login.html"
    success_url = "/"
