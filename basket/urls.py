from django.urls import path

from . import views
app_name='basket'
urlpatterns = [

    path('', views.my_basket,name='my_basket'),
    path('add/', views.basket_add,name='basket_add')
]
