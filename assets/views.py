
from rest_framework import viewsets, permissions
from .models import Asset
from .serializers import AssetSerializer
from authentication.permissions import IsAdminOrManager

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
