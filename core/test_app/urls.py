from django.urls import path
from .views import TestPage, TestPageNew

urlpatterns = [
    path('', TestPage.as_view()),
    path('new/', TestPageNew.as_view()),
]