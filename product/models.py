from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from customer.models import Favourite


class Discount(BaseModel):
    name = models.CharField(max_length=50,
                            verbose_name=_('discount name'),
                            help_text=_('enter the discount'))

    discount = models.PositiveIntegerField(verbose_name=_('discount'),
                                           help_text=_('enter the discount'),
                                           validators=[],
                                           )

    type = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            verbose_name=_('type of discount'))

    def __str__(self):
        return f'{self.id}#  {self.discount}'


class Price(BaseModel):
    price = models.PositiveIntegerField(verbose_name=_('price'),
                                        help_text=_('enter the price'),
                                        blank=False,
                                        null=False,
                                        validators=[])

    unit =models.CharField(max_length=50 ,
                            blank=False,
                            null=False,
                            verbose_name=_('unit of money'))

    def __str__(self):
        return f'{self.price}({self.unit})'


class DiscountCode(BaseModel):
    name = models.CharField(max_length=50,
                            verbose_name=_('discount code'),
                            help_text=_('enter name for discount'),
                            )

    code = models.IntegerField(unique=True,
                               verbose_name=_('discount code'),
                               help_text=' enter code for discount ',
                               )

    type = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            verbose_name=_('type of discountcode'))

    def __str__(self):
        return f'{self.id}#  {self.name}'


class Category(BaseModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               verbose_name=_('enter parent if exist'),
                               default=None,
                               null=True,
                               blank=True)
    name = models.CharField(max_length=100,
                            verbose_name=_('category name'),
                            unique=True,
                            help_text=_('enter the category'))

    def __str__(self):
        return f'{self.id}# {self.name}'


class Brand(BaseModel):
    name = models.CharField(max_length=50,
                            verbose_name=_('brand name'),
                            help_text=_('enter the brand name'),
                            unique=True)

    def __str__(self):
        return f'{self.id}# {self.name}'


class Product(BaseModel):
    brand = models.ForeignKey(Brand,
                              verbose_name=_('barnd name'),
                              on_delete=models.CASCADE)

    category = models.ForeignKey(Category,
                                 verbose_name=_('category'),
                                 on_delete=models.CASCADE,
                                 help_text=_('enter the category'),
                                 blank=False,
                                 null=False)

    price = models.ForeignKey(Price, on_delete=models.CASCADE,
                              verbose_name=_('price'),
                              help_text=_('enter the price'),
                              blank=False,
                              null=False)

    discount = models.ForeignKey(Discount, on_delete=models.CASCADE,
                                 verbose_name=_('discount'),
                                 help_text=_('enter the discount'),
                                 blank=False,
                                 null=False)

    name = models.CharField(verbose_name=_('name'),
                            help_text=_('enter product name'),
                            max_length=200,
                            blank=False,
                            null=False)

    image = models.FileField(_('image'), upload_to=f'',
                             help_text=_('put picture for product'),
                             blank=False,
                             null=False, )

    inventory = models.PositiveIntegerField(verbose_name=_('Inventory'),
                                            blank=False,
                                            null=False)

    view = models.PositiveIntegerField(verbose_name=_('view'),
                                       blank=True,
                                       null=True,
                                       default=0)

    inavailable = models.BooleanField(verbose_name=_('inavailable'),
                                      default= False)

    favourite = models.ForeignKey(Favourite, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}# {self.name}'
