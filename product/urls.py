from django.urls import path

from product.serializer import ProductSerializer
from product.views import ProductView, product_api

urlpatterns = [
    path('product/',ProductView.as_view(), name = 'home'),
    path('myapi/',product_api,name='home')

]


