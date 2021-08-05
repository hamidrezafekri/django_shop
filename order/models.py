from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from customer.models import Favourite, Customer
from product.models import *

class OrderItem(BaseModel):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_('product'),
                                help_text='choose a product',
                                null=False,blank=False)


    customer = models.ForeignKey(Customer,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(verbose_name=_('order quantity'),
                                           default= 1)


    ordered = models.BooleanField(default=False)




    def __str__(self):f'{Product.name}'



class Order(BaseModel):
    orderitem = models.ForeignKey(OrderItem,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('add order'),
                                  )

    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 verbose_name=(_('customer')))



    status = models.ForeignKey('OrderStatus',
                               on_delete=models.CASCADE)


    def __str__(self):
        return f'{OrderItem.product}--{Customer.first_name}{Customer.last_name}'



class OrderStatus(BaseModel):
    status = models.CharField(max_length=50,
                              verbose_name=_('status'),
                              help_text=_('enter the order status'))


    def __str__(self):
        return self.status




class Oredr(BaseModel):

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






