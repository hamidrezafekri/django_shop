from django.test import TestCase
from .models import *
# Create your tests here.


class ProductTest(TestCase):

    def setUp(self) -> None:
        self.brand1 =Brand.objects.create(
            name= 'sumsong'
        )

        self.category1 = Categori.objects.create(
            name= 'cellphone'
        )

        self.price1 = Price.objects.create(
            price='500000'
        )

        self.discount= Discount.objects.create(
            name= 'rooz'








        )


