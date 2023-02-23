from rest_framework import permissions

class PermissionUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_employee is False:
            return obj.email == request.user.email
        return True
