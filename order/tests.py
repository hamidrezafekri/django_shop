from django.test import TestCase

from customer.models import Customer
from order.models import Order, OrderStatus, OrderItem
from product.models import *


class Subtotal(TestCase):
    def setUp(self) -> None:
        self.customer2 = Customer.objects.create(
            username='mamad',
            password='hamidfard',
            email='hamidreza@gmail.com',
            phone='09123456789'
        )
        print(self.customer2)

        self.status1 = OrderStatus.objects.create(status='cancled')
        print(self.status1)
        self.order1 = Order.objects.create(
            customer=self.customer2,
            status=self.status1
        )
        self.discount_1 = Discount.objects.create(discount=5, type='percent')
        self.category_1 = Category.objects.create(name='akbar')
        self.brand_1 = Brand.objects.create(name='LG', image=None)
        self.image_1 = Image.objects.create(image=None, product_id=1)
        self.price_1 = Price.objects.create(price=50000, unit='toman')
        self.product_1 = Product.objects.create(
            brand=self.brand_1,
            category=self.category_1,
            price=self.price_1,
            discount=self.discount_1,
            name='k500',
            inventory=20
        )
        print(self.product_1)
        self.discount_2 = Discount.objects.create()
        self.category_1 = Category.objects.create(name='akbar1')
        self.brand_2 = Brand.objects.create(name='samsung', image=None)
        self.image_1 = Image.objects.create(image=None, product_id=1)
        self.price_2 = Price.objects.create(price=30000, unit='toman')
        self.product_2 = Product.objects.create(
            brand=self.brand_2,
            category=self.category_1,
            price=self.price_2,
            discount=self.discount_2,
            name='k700',
            inventory=20)
        print(self.product_2)

        self.order_item1 = OrderItem.objects.create(
            customer=self.customer2,
            product=self.product_1,
            quantity=3,
            order=self.order1

        )
        print(self.order_item1)
        self.order_item2 = OrderItem.objects.create(
            customer=self.customer2,
            product=self.product_2,
            quantity=3,
            order=self.order1

        )
        print(self.order_item2)

    def test1_calculate_item_total(self):
        print(self.order_item1.total_price_order_item)
        self.assertEqual(self.order_item1.total_price_order_item, 142500)

    def test2_calculate_item_total(self):
        print(self.order_item2.total_price_order_item)
        self.assertEqual(self.order_item2.total_price_order_item, 90000)

    def test3_calculate_order_total(self):
        self.assertEqual(self.order1.sub_total_order, 232500)


    def test4_orderitem_discount(self):
        self.assertEqual(self.order_item1.discount_order_item,7500)

    def test5_order_total_discount(self):
        return self.assertEqual(self.order1.sub_total_dicount_order,7500)
