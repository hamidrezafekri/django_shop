from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product.models import Product
from .basket import Basket


def my_basket(request):
    basket = Basket(request)
    return render(request ,'basket/basket.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('id'))
        product_qty = int(request.POST.get('qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


