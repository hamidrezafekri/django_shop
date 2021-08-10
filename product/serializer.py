from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'inventory']
        extra_kwargs = {
            'id': {'read_only': True}
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'