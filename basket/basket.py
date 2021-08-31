from decimal import Decimal

from product.models import Product

CART_SESSION_ID = 'session_key'


class Basket():

    def add(self, product, qty):

        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {'price': product.price.price, 'qty': qty,
                                       'discount': product.calculate_discount(),
                                       'final_price': product.product_final_price()}
        self.session.modified = True

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(CART_SESSION_ID)
        if CART_SESSION_ID not in request.session:
            basket = self.session[CART_SESSION_ID] = {}
        self.basket = basket

    def __len__(self):
        return sum(int(item['qty']) for item in self.basket.values())

    def __iter__(self):

        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in self.basket.values():
            item['total_price'] = int(item['price']) * item['qty']
            yield item

    def get_total_price(self):
        return sum(item['price'] * item['qty'] for item in self.basket.values())

    def total_discount(self):
        return sum(item['discount'] * item['qty'] for item in self.basket.values())


    def final_price(self):
        return sum(item['final_price'] * item['qty'] for item in self.basket.values())



