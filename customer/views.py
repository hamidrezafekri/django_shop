from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import View
from rest_framework.generics import *
from customer.models import Customer, Address
from customer.serializer import CustomerSerilazlizer, AddressSerializer, \
    AddressBriefSerializer, CustomerBriefSerializer
from .permissions import *
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView


class CustomerListApiView(ListAPIView):
    serializer_class = CustomerBriefSerializer
    queryset = Customer.objects.filter(deleted=False)
    permission_classes = [OnlySuperUser]


class CustomerDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerilazlizer
    queryset = Customer.objects.filter(deleted=False)
    permission_classes = [OnlyOwner]


class AddressListApiView(ListAPIView):
    serializer_class = AddressBriefSerializer

    def get_queryset(self):
        return Address.objects.filter(customer__user_id=self.request.user.id, deleted=False)


class AddressDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.filter(deleted=False)
    permission_classes = [OnlyOwner]


class LoginPage(LoginView):
    template_name = 'login.html'
    success_url = 'accounts/profile'


class LoggedInView(PermissionRequiredMixin, View):
    permission_required = 'auth.see_profile'

    def get(self, request, *args, **kwargs):
        return render(request, 'main_page.html')


class Outview(LogoutView):
    next_page = 'login'





class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'registertion.html'
    success_url = 'login.html'
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

