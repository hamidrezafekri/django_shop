from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from basket.basket import Basket

from .models import Order, OrderItem
from .serializer import *


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(customer_id=user_id,
                                         order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'],
                                         quantity=item['qty'])

        response = JsonResponse({'success': 'Return something'})
        return response


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders


class OrderDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.all() if self.request.user.is_superuser else Order.objects.filter(
            id=self.request.user.id)


class OrderItemApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializers
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return OrderItem.objects.all() if self.request.user.is_superuser else OrderItem.objects.filter(
            id=self.request.user.id)


