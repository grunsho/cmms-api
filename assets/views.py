
from rest_framework import viewsets, permissions
from .models import Asset
from .serializers import AssetSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # Permiso por defecto: solo usuarios autenticados pueden ver
    permission_classes = [permissions.IsAuthenticated]

    # Opcional: Personalizar permisos para diferentes operaciones o roles
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Solo administradores o gerentes pueden crear, actualizar o eliminar
            self.permission_classes = [permissions.IsAuthenticated, IsAdminOrManager] # Creamos este permiso
        else:
            # Todos los autenticados pueden listar y recuperar (ver detalles)
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

# Permiso personalizado para roles de Admin o Manager
class IsAdminOrManager(permissions.BasePermission):
    """
    Permiso personalizado para permitir acceso solo a usuarios 'admin' o 'manager'.
    """
    def has_permission(self, request, view):
        # Permite acceso si el usuario está autenticado y tiene rol 'admin' o 'manager'
        return request.user and request.user.is_authenticated and \
               request.user.role in ['admin', 'manager']

    def has_object_permission(self, request, view, obj):
        # Permite acceso si el usuario está autenticado y tiene rol 'admin' o 'manager'
        # Esto es útil si quieres control a nivel de objeto, pero para activos completos,
        # has_permission suele ser suficiente.
        return request.user and request.user.is_authenticated and \
               request.user.role in ['admin', 'manager']