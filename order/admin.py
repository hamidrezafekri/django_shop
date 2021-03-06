from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


def logical_delete(modeladmin, request, queryset):
    queryset.update(deleted=True)


logical_delete.short_description = "logical delete"


class OrderItemAdmin(admin.ModelAdmin):
    fieldsets = [(_('order items'),
                  {'fields': ['product','customer','quantity','order']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'deleted']})]

    search_fields = ['product','customer','quantity']
    list_filter = ['quantity']
    actions = [logical_delete]


class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [(_('order items'),
                  {'fields': ['customer','status']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'deleted']})]

    search_fields = ['customer','status']
    actions = [logical_delete]
    inlines = [OrderItemInLine]


class OrderStatusAdmin(admin.ModelAdmin):
    fieldsets = [(_('status'),
                  {'fields': ['status']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'deleted']})]

    search_fields = ['status']
    list_filter = ['status']
    actions = [logical_delete]






admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)


