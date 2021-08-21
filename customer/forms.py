from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request

from customer.models import Customer, Address


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control p-3  list-group', }),
                   'first_name': forms.TextInput(attrs={'class': 'form-control p-3  list-group', }),
                   'last_name': forms.TextInput(attrs={'class': 'form-control p-3  list-group', }),
                   'email': forms.TextInput(attrs={'class': 'form-control p-3 list-group' , }),
                   'phone': forms.TextInput(attrs={'class': 'form-control p-3  list-group list', }),
                   'password1': forms.TextInput(attrs={'class': 'form-control p-3  list-group', }),
                   'password2': forms.TextInput(attrs={'class': 'form-control p-3  list-group', })

                   }


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['deleted', 'delete_time_stamp', 'customer']

        widgets = {'country': forms.TextInput(attrs={'class': 'form-control p-3 w-2', }),
                   'province': forms.TextInput(attrs={'class': 'form-control', }),
                   'city': forms.TextInput(attrs={'class': 'form-control', }),
                   'postal_address': forms.TextInput(attrs={'class': 'form-control', })

                   }
