from rest_framework import serializers

from order.models import Order, OrderItem


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = []


class OrderItemSerializers(serializers.ModelSerializer):
    model = OrderItem
    exclude = []
