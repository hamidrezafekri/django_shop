from django import forms
from django.contrib.auth.forms import UserCreationForm
from customer.models import Customer


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'national_code', 'password1', 'password2']