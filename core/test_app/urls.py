from django.urls import path
from .views import TestPage, TestPageNew

urlpatterns = [
    path('', TestPage.as_view(), name='test_page'),
    path('new/', TestPageNew.as_view(), name='test_page_new'),
]
