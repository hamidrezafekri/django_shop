from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.views.generic import ListView, DetailView
from .serializer import ProductSerializer, ProductBriefSerializer, CategorySerializer


class ProductView(ListView):
    template_name = 'product/../templates/product.html'
    model = Product



class ProductDetailView(DetailView):
    template_name = 'product/../templates/product_detail.html'
    model = Product


class CategoryView(ListView):
    template_name = 'product/../templates/category.html'
    model = Category


from rest_framework.generics import *


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(deleted= False)


class ProductDetailApi(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(deleted=False)
    lookup_url_kwarg = 'slug'
    lookup_field = 'id'


class ProductEditApi(UpdateAPIView):
    serializer_class = ProductBriefSerializer
    queryset = Product.objects.filter(deleted=False)



class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(deleted=False)




