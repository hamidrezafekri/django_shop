from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from customer.models import Favourite, Customer
from product.models import *


class OrderItem(BaseModel):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_('product'),
                                help_text='choose a product',
                                null=False, blank=False)

    customer = models.ForeignKey(Customer,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(verbose_name=_('order quantity'),
                                           default=1)

    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              verbose_name=_('add order'),
                              )

    def __str__(self):
        return f'{self.product.name}'

    def check_inventory(self):
        if not self.quantity <= self.product.inventory:
            raise Exception(_('inventory is not enough'))

    @property
    def total_price_order_item(self):
        return self.product.product_final_price() * self.quantity


class Order(BaseModel):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 verbose_name=(_('customer')))

    status = models.ForeignKey('OrderStatus',
                               on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.customer.username}'


STATUS = [('processing', 'processing'), ('delivered', 'delivered'), ('cancled', 'cancled'),('payed','payed')]


class OrderStatus(BaseModel):
    status = models.CharField(max_length=50,
                              verbose_name=_('status'),
                              help_text=_('enter the order status'),
                              choices=STATUS)

    def __str__(self):
        return self.status
