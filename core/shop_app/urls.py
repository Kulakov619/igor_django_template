from django.urls import path, include
from shop_app import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'products', views.ProductsViewSet)


urlpatterns = [
    path("", include(router.urls)),
]