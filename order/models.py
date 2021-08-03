from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from product.models import *
# Create your models here.
class OrderItem(BaseModel):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_('product'),
                                help_text='choose a product',
                                null=False,blank=False)



class Order(BaseModel):
    orderitem = models.ForeignKey(OrderItem,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('add order'),
                                  )

    quantity = models.PositiveIntegerField(verbose_name="quantity",
                                           default=1,
                                           null=False,
                                           blank=False)

    reciept = models.ForeignKey('Reciept',on_delete=models.CASCADE)



class OrderStatus(BaseModel):
    status = models.CharField(max_length=50,
                              verbose_name=_('status'),
                              help_text=_('enter the order status'))




class Reciept(BaseModel):

    orderstatus =models.ForeignKey(OrderStatus,
                                   on_delete=models.CASCADE,
                                   verbose_name=('order status'),
                                   help_text='enter the status',
                                   blank=False,
                                   null=False)

    discountcode= models.ForeignKey(DiscountCode,
                                    on_delete=models.CASCADE,
                                    verbose_name=_('discount code'))







