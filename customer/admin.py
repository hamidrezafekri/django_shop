from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from order.admin import logical_delete
from .models import Customer, Favourite,Address

class AddressAdmin(admin.ModelAdmin):
    fieldsets = [(_('add address'),
                  {'fields': ['country','province','city','postal_address']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp','deleted']})]

    search_fields = ['product', 'customer', 'quantity', 'ordered']
    list_filter = ['product', 'customer', 'quantity', 'ordered']
    actions = [logical_delete]


admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Favourite)
