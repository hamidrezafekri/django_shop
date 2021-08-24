from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from rest_framework.response import Response

from product.models import Product
from .basket import Basket


def my_basket(request):
    return render(request, 'basket/basket.html')


def basket_add(request):
    basket = Basket(request)
    if request.method == 'POST':
        print('post')
        product_id = request.POST.get('id')
        price = Product.objects.get(id=product_id).price.price
        print(price)
        product_qty = request.POST.get('qty')

        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        response = JsonResponse({'qty': product_qty, 'price': price})
        return response
