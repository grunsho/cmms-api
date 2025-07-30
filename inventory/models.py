from django.db import models
import uuid

class Part(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nombre de la Pieza")
    sku = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="SKU/Número de Parte")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    quantity = models.IntegerField(default=0, verbose_name="Cantidad en Stock")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ubicación de Almacén")
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Costo Unitario")
    supplier = models.CharField(max_length=255, blank=True, null=True, verbose_name="Proveedor Principal")
    reorder_point = models.IntegerField(default=0, verbose_name="Punto de Reorden") # Stock mínimo para reordenar
    last_reordered_date = models.DateField(null=True, blank=True, verbose_name="Última Reorden")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pieza"
        verbose_name_plural = "Piezas"
        ordering = ['name'] # Ordenar por nombre por defecto

    def __str__(self):
        return self.name