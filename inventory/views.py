from rest_framework import viewsets, permissions
from .models import Part
from .serializers import PartSerializer
from authentication.models import User # Asumiendo que User es el modelo de usuario personalizado
from authentication.permissions import IsAdminOrManager

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAuthenticated] # Por defecto, requiere autenticación

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Solo administradores o gerentes pueden crear, actualizar o eliminar piezas
            self.permission_classes = [permissions.IsAuthenticated, IsAdminOrManager]
        else:
            # Todos los autenticados pueden listar y recuperar (ver detalles)
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()