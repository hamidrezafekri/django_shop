from rest_framework import serializers

from .models import Product





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id','image','view']

        extra_kwargs = {
            'id': {'read_only': True}
        }