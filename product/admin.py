from django.contrib import admin

# Register your models here.
from product.models import Product, Details


class DetailInline(admin.TabularInline):
    model = Details
    extra = 3


class ProductModelAdmin(admin.ModelAdmin):
    inlines = [DetailInline]

admin.site.register(Details)
admin.site.register(Product,ProductModelAdmin)