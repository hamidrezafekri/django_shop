import re

from django.core.exceptions import ValidationError
from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, User

def phone_validation(phone):
    pattern = r'(^09\d{9}$)|(^\+989\d{9}$)'
    if not bool(re.match(pattern, phone)):
        raise ValidationError('Phone number is wrong!!!')


class Customer(BaseModel, User):
    phone = models.CharField(max_length=15,
                             verbose_name=_('phone number'),
                             unique=True,
                             null=False,
                             blank=False,
                             validators=[phone_validation])


class Address(BaseModel):
    country = models.CharField(max_length=50,
                               verbose_name=_('country'))

    province = models.CharField(max_length=50,
                                verbose_name=_('province'))

    city = models.CharField(max_length=50,
                            verbose_name=_('city'))

    postal_address = models.CharField(max_length=250,
                                      verbose_name=_('postal address'))

    customer = models.ForeignKey('Customer',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f''


class Favourite(BaseModel):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)

    favourite = models.BooleanField(verbose_name='like product',
                                    default=False)

    def __str__(self):
        return self.customer.last_name
