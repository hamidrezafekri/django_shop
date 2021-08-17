from django.urls import path

from customer.views import *





app_name = 'customer'
urlpatterns = [
    path('customerlist/', CustomerListApiView.as_view(), name='customer_list_api'),
    path('customerdetail/<int:pk>', CustomerDetailApiView.as_view(), name='customer_detail_api'),
    path('addresslist/', AddressListApiView.as_view(), name='Address_list_api_view'),
    path('addressdetail/', AddressDetailApiView.as_view(), name='Address_detail_api_view'),
    path('login/', LoginPage.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', Outview.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='signup'),
    path('create_address/', AddressCreateView.as_view(), name='add_address'),

]