from django.urls import path
from .views import TestPage, TestPageNew, CreatePost


urlpatterns = [
    path('', TestPage.as_view(), name='test_page'),
    path('new/', TestPageNew.as_view(), name='test_page_new'),
    path('create/', CreatePost.as_view(), name='create')
]
