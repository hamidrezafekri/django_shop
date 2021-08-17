from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request

from customer.models import Customer, Address


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name','email','phone', 'password1', 'password2']


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude=['customer']




