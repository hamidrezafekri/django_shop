from rest_framework import permissions


class OnlySuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
         return request.user.is_superuser




class OnlyOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer.user_ptr_id == request.user.id



