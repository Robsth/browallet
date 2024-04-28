from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed


class CreateReadPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
        raise MethodNotAllowed(request.method)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        raise MethodNotAllowed(request.method)
