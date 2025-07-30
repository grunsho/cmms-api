from djoser.views import UserViewSet as DjoserViewSet
from rest_framework import permissions
from .models import User

# Permiso personalizado para roles de Admin
class IsAdmin(permissions.BasePermission):
    """
    Permiso personalizado para permitir acceso solo a usuarios 'admin'
    """
    def has_permission(self, request, view):
        # Permite acceso si el usuario está autenticado y tiene rol 'admin'
        return request.user and request.user.is_authenticated and \
               isinstance(request.user, User) and \
               request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        # Permite acceso si el usuario está autenticado y tiene rol 'admin'
        # o si el usuario está intentando ver/editar su propio perfil.
        # Esto permite a los usuarios ver su propio perfil aunque no sean admin.
        if request.user and request.user.is_authenticated and isinstance(request.user, User):
            if request.user.role == 'admin':
                return True
            # Permite a los usuarios regulares acceder a su propio perfil (GET, PATCH)
            return request.user == obj and request.method in permissions.SAFE_METHODS # SAFE_METHODS son GET, HEAD, OPTIONS

class UserManagementViewSet(DjoserViewSet):
    # Djoser ya usa su propio serializer para el modelo de usuario.
    # Aquí estamos sobrescribiendo para ajustar los permisos.
    def get_permissions(self):
        # Para acciones de lista y detalle, crear, actualizar, eliminar
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, IsAdmin]
        else:
            # Djoser por defecto para el resto de acciones (ej. set_password, me, etc.)
            self.permission_classes = DjoserViewSet.permission_classes
        return super().get_permissions()
    
    # Sobrescribimos el queryset para la acción 'list para obtener todos los usuarios 
    # Por defecto, Djoser's list puede ser limitado
    def get_queryset(self):
        if self.action == 'list':
            return User.objects.all().order_by('username')
        return super().get_queryset() 