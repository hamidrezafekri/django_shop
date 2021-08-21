from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import request, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from rest_framework.generics import *
from customer.models import Address
from customer.serializer import CustomerSerilazlizer, AddressSerializer, \
    AddressBriefSerializer, CustomerBriefSerializer
from .permissions import *
from .forms import UserRegisterForm, AddressCreateForm
from django.views.generic.edit import CreateView


class CustomerListApiView(ListAPIView):
    serializer_class = CustomerBriefSerializer
    queryset = Customer.objects.filter(deleted=False)
    permission_classes = [permissions.IsAdminUser]


class CustomerDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerilazlizer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all() if self.request.user.is_superuser else Customer.objects.filter(
            id=self.request.user.id)


class AddressListApiView(ListAPIView):
    serializer_class = AddressBriefSerializer

    def get_queryset(self):
        return Address.objects.filter(customer=self.request.user.id, deleted=False)


class AddressDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.filter(deleted=False)
    permission_classes = [OnlyOwner]


# --------------------------------------------------------------------------
class LoginPage(LoginView):
    template_name = 'customer/login.html'
    success_url = reverse_lazy('customer:panel')


class Profile(LoginRequiredMixin, View):
    permission_required = 'auth.see_profile'

    def get(self, request, *args, **kwargs):
        return render(request, 'customer/customer_panel.html')





class Outview(LogoutView):
    next_page = reverse_lazy('customer:login')


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'customer/registertion.html'
    success_url = reverse_lazy('customer:login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class AddressCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'auth.see_profile'
    template_name = 'customer/create_address.html'
    form_class = AddressCreateForm
    success_url = reverse_lazy('customer:panel')



    def form_valid(self, form):
        address = form.save(commit=False)
        print(address)
        address.customer = Customer.objects.get(user_ptr_id=self.request.user.id)
        return super().form_valid(form)


class AddressView(LoginRequiredMixin,ListView):
    permission_denied_message = 'first login'
    template_name = 'customer/show_address.html'


    def get_queryset(self):
        return Address.objects.filter(customer_id=self.request.user.id)


class PersonalInfo(LoginRequiredMixin,ListView):
    permission_denied_message = 'first login'
    template_name = 'customer/personal_info.html'


    def get_queryset(self):
        return Customer.objects.filter(user_ptr_id=self.request.user.id)



class CustomerPanel(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'customer/customer_panel.html')


