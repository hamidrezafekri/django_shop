from django.test import TestCase
from .models import *


class customer_test(TestCase):
    def test_customer(self):
        self.customer = Customer.objects.create(
            username='mamad',
            password= 'hamidfekri',
            email='hamidreza@gmail.com',
            phone= '09337272512'
        )


class address_test(TestCase):


    def setUp(self) -> None:
        self.customer2 = Customer.objects.create(
            username='mamad',
            password='hamidfard',
            email='hamidreza@gmail.com',
            phone='09123456789'
        )
    def test_address(self):
        self.address1 = Address.objects.create(

            country= 'iran',
            province= 'tehran',
            city='tehran',
            postal_address='akbar street',
            customer=self.customer2

        )
