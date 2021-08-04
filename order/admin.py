from django.contrib import admin
from django.utils.translation import gettext_lazy as _


def logical_delete(modeladmin, request, queryset):
    queryset.update(deleted=True)


logical_delete.short_description = "logical delete"

class OrderItemAdmin(admin.ModelAdmin):
    fieldsets = [(_('order items'),
                  {'fields': ['product','favourite']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'is_deleted']})]

    search_fields = ['product','favourite']
    list_filter = ['product','favourite']
    actions = [logical_delete]


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [(_('order items'),
                  {'fields': ['product', 'favourite']}),
                 (_('delete_status'),
                  {'fields': ['delete_time_stamp', 'is_deleted']})]

    search_fields = ['product', 'favourite']
    list_filter = ['product', 'favourite']
    actions = [logical_delete]