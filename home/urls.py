from django.urls import path

from home.views import DiscountProducts

urlpatterns=[
    path('',DiscountProducts.as_view(),name='home')
]