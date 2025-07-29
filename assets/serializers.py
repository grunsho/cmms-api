from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__' # Incluye todos los campos del modelo
        # También puedes especificar los campos explícitamente:
        # fields = ['id', 'name', 'description', 'location', 'serial_number',
        #           'purchase_date', 'last_maintenance_date', 'next_maintenance_date',
        #           'status', 'asset_type', 'manufacturer', 'model', 'warranty_end_date']