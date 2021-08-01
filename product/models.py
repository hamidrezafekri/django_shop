from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from core.models import BaseModel


class Discount(BaseModel):
    pass


class Price(BaseModel):
    pass


class DiscountCode(BaseModel):
    pass


class Category(BaseModel):
    pass


class Details(BaseModel):
    product_detail = models.ForeignKey('Product', verbose_name=_('add details'),on_delete=models.CASCADE)
    feature = models.CharField(max_length=50,verbose_name=_('feature'))
    explain = models.CharField(max_length=50,verbose_name=_('explain'))


class Product(BaseModel):
    name = models.CharField(verbose_name=_('name'),
                            help_text=_('enter product name'),
                            max_length=200,
                            blank=False,
                            null=False)

    Image = models.FileField(_('image'), upload_to='Product',
                             help_text=_('put picture for product'),
                             blank=False,
                             null=False)

    inventory = models.IntegerField(verbose_name=_('Inventory'),
                                    blank=False,
                                    null=False)
