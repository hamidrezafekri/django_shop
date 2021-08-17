from django.test import TestCase
from product.models import *


class DiscountTest(TestCase):

    def test1_type_amount(self):
        self.dis1 = Discount.objects.create(name='test_dis1', discount=20000, type='amount')
        self.dis2 = Discount.objects.create(name='test_dis2', discount=20000, type='amount')

    def test2_type_percent(self):
        self.dis1 = Discount.objects.create(name='test_dis3', discount=20, type='percent')
        self.dis2 = Discount.objects.create(name='test_dis4', discount=10, type='percent')


class CategoryTest(TestCase):

    def test1_make_object(self):
        self.cat1 = Category.objects.create(category_name='laptop')


class BrandTest(TestCase):

    def test1_make_object(self):
        self.brand = Brand.objects.create(brand_name='asus')


class ProductTest(TestCase):

    def setUp(self) -> None:
        self.discount_1 = Discount.objects.create(
            discount=5,
            type='percent'
        )

        self.category_1 = Category.objects.create(name='akbar')
        self.brand_1 = Brand.objects.create(name='LG', image=None)
        self.image_1 = Image.objects.create(image=None, product_id=1)
        self.price_1 = Price.objects.create(price=20000, unit='toman')
        self.product_1 = Product.objects.create(
            brand=self.brand_1,
            category=self.category_1,
            price=self.price_1,
            discount=self.discount_1,
            name='k500',
            inventory=20
        )

    def test1_final_price(self):
        self.assertEqual(self.product_1.product_final_price(), 19000)

