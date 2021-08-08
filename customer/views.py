from django.shortcuts import render
from rest_framework.generics import *
# Create your views here.
from customer.models import Customer, Address
from customer.serializer import CustomerSerilazlizer, AddressSerializer
from .permissions import *

class CustomerListApiView(ListAPIView):
    serializer_class = CustomerSerilazlizer
    queryset = Customer.objects.all()
    permission_classes = [OnlySuperUser]



class CustomerDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerilazlizer
    queryset = Customer.objects.all()
    permission_classes = [OnlyOwner]



class AddressLoggedInUser(ListAPIView):
    serializer_class = AddressSerializer
    def get_queryset(self):
        return Address.objects.filter(customer__user_id=self.request.user.id)
