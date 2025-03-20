from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Product
from .serializers import ProductSerializer, ProductListSerializer, ProductCreateSerializer



class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'create':
            return ProductCreateSerializer
        return super().get_serializer_class()