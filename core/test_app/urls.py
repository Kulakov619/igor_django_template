from django.urls import path
from .views import TestPage, TestPageNew, CreatePost, DeletePost, DetailPost, ListPost, UpdatePost

urlpatterns = [
    path('', TestPage.as_view(), name='test_page'),
    path('new/', TestPageNew.as_view(), name='test_page_new'),
    path('create/', CreatePost.as_view(), name='create'),
    path('update/<int:id>/', UpdatePost.as_view(), name='update'),
    path('delete/<int:id>/', DeletePost.as_view(), name='delete'),
    path('detail/<int:id>/', DetailPost.as_view(), name='detail'),
    path('list/', ListPost.as_view(), name='list')
]

