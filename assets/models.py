from django.db import models
import uuid

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre del Activo')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    location = models.CharField(max_length=255, verbose_name='Ubicación')
    serial_number = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name='Número de Serie')
    purchase_date = models.DateField(blank=True, null=True, verbose_name='Fecha de Compra')
    last_maintenance_date = models.DateField(blank=True, null=True, verbose_name='Último Mantenimiento')
    next_maintenance_date = models.DateField(blank=True, null=True, verbose_name='Próximo Mantenimiento')

    STATUS_CHOICES = [
        ('operational', 'Operacional'),
        ('under_maintenance', 'En Mantenimiento'),
        ('retired', 'Retirado'),
        ('critical', 'Crítico'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='operational', verbose_name='Estado')
    
    ASSET_TYPE_CHOICES = [
        ('vehicle', 'Vehículo'),
        ('machine', 'Máquina'),
        ('building', 'Edificio'),
        ('tool', 'Herramienta'),
        ('equipment', 'Equipo General'),
        ('other', 'Otro'),
    ]
    asset_type = models.CharField(max_length=50, choices=ASSET_TYPE_CHOICES, default='equipment', verbose_name="Tipo de Activo")

    # Campos adicionales que podríamos agregar a futuro
    manufacturer = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fabricante")
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name="Modelo")
    warranty_end_date = models.DateField(blank=True, null=True, verbose_name="Fin de Garantía")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'
        ordering = ['name']
    
    def __str__(self):
        return self.name