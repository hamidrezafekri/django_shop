from rest_framework import serializers
from .models import Address,Customer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = []


class CustomerSerilazlizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

