from django.views.generic import ListView, TemplateView

from product.models import Product


class DiscountProducts(TemplateView):
    template_name = 'home/home.html'
    dis_product = Product.objects.filter(discount__discount__gt=0)[:4]
    new_product = Product.objects.order_by('-id')[:4]
    extra_context = {'disproducts': dis_product, 'new_products': new_product}

