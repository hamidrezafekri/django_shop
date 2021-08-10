from django.urls import path
from product.views import ProductView, ProductListApiView, ProductDetailApi, \
    ProductDetailView, CategoryView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product'),
    path('product/<slug>', ProductDetailView.as_view(), name='product_detail'),
    path('category/', CategoryView.as_view(), name='category_list'),

    path('product_api/', ProductListApiView.as_view()),
    path('product_detail_api/<int:pk>', ProductDetailApi.as_view()),

]