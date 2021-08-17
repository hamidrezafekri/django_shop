from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from product.models import Product, Category, \
    DiscountCode, Price, Discount, Brand, Image
from django_mptt_admin.admin import DjangoMpttAdmin


def logical_delete(modeladmin, request, queryset):
    queryset.update(deleted=True)


logical_delete.short_description = "logical delete"


class BrandAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('add_brand'),
         {'fields': ['name']}),
        (_('delete_status'),
         {'fields': ['delete_time_stamp', 'deleted']})]

    search_fields = ['name']

    list_filter = ['name']

    actions = [logical_delete]


class CategoryAdmin(DjangoMpttAdmin):
    # fieldsets = [(_('add catergory'),
    #               {'fields': ['parent', 'name', 'slug']}),
    #              (_('delete_status'),
    #               {'fields': ['delete_time_stamp', 'deleted']})]
    # search_fields = ['parent', 'name', 'slug']
    # list_filter = ['name', 'parent', 'slug']
    # actions = [logical_delete]
    pass


class DiscountCodeAdmin(admin.ModelAdmin):
    fieldsets = [(_('add discount_code'),
                  {'fields': ['name', 'code', 'type']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'deleted']})]

    search_fields = ['name', 'code', 'type']
    list_filter = ['name', 'code', 'type']
    actions = [logical_delete]


class ImageInLine(admin.StackedInline):
    model = Image
    extra = 5


class DiscountAdmin(admin.ModelAdmin):
    fieldsets = [(_('add discount'),
                  {'fields': ['name', 'discount', 'type']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'deleted']})]

    search_fields = ['name', 'discount', 'type']
    list_filter = ['name', 'type']
    actions = [logical_delete]


class PriceAdmin(admin.ModelAdmin):
    fieldsets = [(_('add price'),
                  {'fields': ['price', 'unit']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'deleted']})]

    search_fields = ['price', 'unit']
    list_filter = ['unit']
    actions = [logical_delete]


class ProductModelAdmin(admin.ModelAdmin):
    fieldsets = [(_('add product'),
                  {'fields': ['name', 'inventory', 'inavailable', 'price',
                              'category', 'brand', 'discount', 'score', 'view', 'slug','main_image']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'deleted'],
                   })]

    search_fields = ['name', 'inventory', 'inavailable', 'slug']
    list_filter = ['name', 'inventory', 'inavailable', 'slug']
    actions = [logical_delete]
    inlines = [ImageInLine]



admin.site.register(Discount, DiscountAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductModelAdmin)
