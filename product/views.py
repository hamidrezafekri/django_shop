from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *
# Create your views here.
from django.views.generic import ListView, DetailView

from .serializer import ProductSerializer


class ProductView(ListView):
    template_name = 'product/home.html'
    model = Product


class ProductDetailView(DetailView):
    pass



@csrf_exempt
def product_api(request):
    if request.method == 'GET':
        # List of Questions!
        products = Product.objects.all()
        p = ProductSerializer(products, many=True)
        return JsonResponse({
            "product": p.data
        })
    elif request.method == 'POST':
        # Create new instance!
        p = ProductSerializer(data=request.POST)
        print(request.POST)
        if p.is_valid():
            p.save()
            print(request.POST)
            return JsonResponse(p.data)
        else:
            return JsonResponse(p.errors)
