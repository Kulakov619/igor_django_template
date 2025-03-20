from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'description',
            'imageUrl',
            'category'
        )


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'imageUrl'
        )


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'description',
            'imageUrl',
            'category'
        )