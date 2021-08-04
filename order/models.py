from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from customer.models import Favourite, Customer
from product.models import *
# Create your models here.
class OrderItem(BaseModel):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_('product'),
                                help_text='choose a product',
                                null=False,blank=False)

    favourite = models.ForeignKey(Favourite,on_delete=models.CASCADE)



class Order(BaseModel):
    orderitem = models.ForeignKey(OrderItem,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('add order'),
                                  )

    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 verbose_name=(_('customer')))

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

    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 verbose_name=(_('customer')))

    discountcode= models.ForeignKey(DiscountCode,
                                    on_delete=models.CASCADE,
                                    verbose_name=_('discount code'))


    def __str__(self):
        return f'{Customer.first_name}--{OrderStatus.status}'






