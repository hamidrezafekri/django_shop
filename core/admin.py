from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


def logical_delete(modeladmin, request, queryset):
    queryset.update(deleted=True)

class UserAdmin(admin.ModelAdmin):
    actions = [logical_delete]



admin.site.register(User,UserAdmin)