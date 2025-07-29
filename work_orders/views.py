from rest_framework import viewsets, permissions
from .models import WorkOrder
from .serializers import WorkOrderSerializer
from authentication.permissions import IsAdminOrManager
from rest_framework import permissions

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            # Solo administradores o gerentes pueden crear o eliminar órdenes
            self.permission_classes = [permissions.IsAuthenticated, IsAdminOrManager]
        elif self.action in ['update', 'partial_update']:
            # Admin/Manager pueden actualizar cualquier orden
            # Técnicos solo pueden actualizar su propia orden (ej. cambiar estado a 'completed')
            self.permission_classes = [permissions.IsAuthenticated, IsAdminOrManagerOrAssignedTechnician] # Nuevo permiso
        else:
            # Todos los autenticados pueden listar y recuperar
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    # Opcional: Filtrar órdenes por el usuario asignado si no es admin/manager
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated and user.role == 'technician':
            # Los técnicos solo ven las órdenes asignadas a ellos
            queryset = queryset.filter(assigned_to=user)
        return queryset

# Nuevo permiso personalizado para Admin, Manager o Técnico Asignado
class IsAdminOrManagerOrAssignedTechnician(permissions.BasePermission):
    """
    Permiso personalizado para permitir acceso a Admin, Manager,
    o al técnico asignado a la orden de trabajo.
    """
    def has_permission(self, request, view):
        # Permite acceso si el usuario está autenticado
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Si el usuario es admin o manager, tiene permiso
        if request.user.role in ['admin', 'manager']:
            return True
        # Si el usuario es el técnico asignado a esta orden, tiene permiso
        if request.user.role == 'technician' and obj.assigned_to == request.user:
            return True
        return False