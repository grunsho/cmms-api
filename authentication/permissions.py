from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    """
    Permiso personalizado para permitir acceso solo a usuarios 'admin' o 'manager'.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               request.user.role in ['admin', 'manager']

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and \
               request.user.role in ['admin', 'manager']