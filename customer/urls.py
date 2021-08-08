from django.urls import path

from customer.views import *

urlpatterns = [
    path('userlist/', CustomerListApiView.as_view(), name='home'),
    path('userdetail/<int:pk>', CustomerDetailApiView.as_view(), name='home'),
    path('address/', AddressLoggedInUser.as_view(), name='home')
]
