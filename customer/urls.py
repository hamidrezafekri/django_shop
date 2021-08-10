from django.urls import path

from customer.views import *






urlpatterns = [
    path('customerlist/', CustomerListApiView.as_view(), name='customer_list_api'),
    path('customerdetail/<int:pk>', CustomerDetailApiView.as_view(), name='customer_detail_api'),
    path('addresslist/', AddressListApiView.as_view(), name='Address_list_api_view'),
    path('addressdetail/', AddressDetailApiView.as_view(), name='Address_detail_api_view'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logged in /', LoggedInView.as_view(), name='logged in'),
    path('logout/', LoggedInView.as_view(), name='log out'),
    path('register/', UserRegisterView.as_view(), name='signup'),

]