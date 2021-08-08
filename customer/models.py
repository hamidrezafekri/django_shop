from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, User


class Customer(BaseModel):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                )


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
        return f'address'


class Favourite(BaseModel):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)

    favourite = models.BooleanField(verbose_name='like product',
                                    default=False)

    def __str__(self):
        return self.customer.user.last_name
