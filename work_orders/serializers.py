from rest_framework import serializers
from .models import WorkOrder
from assets.serializers import AssetSerializer # Para anidar el activo
from authentication.serializers import UserSerializer # Para anidar el usuario

class WorkOrderSerializer(serializers.ModelSerializer):
    # Campos de solo lectura para mostrar el nombre del activo y el usuario
    asset_name = serializers.CharField(source='asset.name', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)

    class Meta:
        model = WorkOrder
        fields = '__all__' # Incluye todos los campos del modelo
        # También puedes especificar los campos explícitamente:
        # fields = ['id', 'title', 'description', 'asset', 'asset_name',
        #           'assigned_to', 'assigned_to_username', 'status', 'priority',
        #           'due_date', 'completed_at', 'created_at', 'updated_at']