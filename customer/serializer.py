from rest_framework import serializers
from .models import Address, Customer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = []


class AddressBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'customer', 'province']


class CustomerSerilazlizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Customer'
        fields = ['id', 'national_code']
