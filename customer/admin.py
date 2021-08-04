from django.contrib import admin

# Register your models here.
from customer.models import Customer, Favourite,Address

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Favourite)