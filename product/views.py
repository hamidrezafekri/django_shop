from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.views.generic import ListView, DetailView
from .serializer import ProductSerializer


class ProductView(ListView):
    template_name = 'product/product.html'
    model = Product



class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product


class CategoryView(ListView):
    template_name = 'product/category.html'
    model = Category


from rest_framework.generics import *


class ProductListApiView(ListCreateAPIView, ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApi(RetrieveDestroyAPIView,UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'





