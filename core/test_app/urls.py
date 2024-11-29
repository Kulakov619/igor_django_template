from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestPage.as_view(), name='test_page'),
    path('new/', views.TestPageNew.as_view(), name='test_page_new'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('update/<int:id>/', views.UpdatePost.as_view(), name='update'),
    path('delete/<int:id>/', views.DeletePost.as_view(), name='delete'),
    path('detail/<int:id>/', views.DetailPost.as_view(), name='detail'),
    path('list/', views.ListPost.as_view(), name='list')
]

