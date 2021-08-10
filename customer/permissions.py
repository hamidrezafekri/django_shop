from rest_framework import permissions

from core.models import User
from customer.models import Customer


class OnlySuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
         return request.user.is_superuser




class OnlyOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user



