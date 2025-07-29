from django.db import models
import uuid
from assets.models import Asset
from authentication.models import User

class WorkOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name='Título de la Orden')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    
    # Relación con el Activo
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name='work_orders',
        verbose_name='Activo Asociado'
    )
    
    # Relación con el técnico asociado
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_work_orders',
        verbose_name='Asignado a'
    )
    
    STATUS_CHOICES = [
        ('open', 'Abierta'),
        ('in_progress', 'En Progreso'),
        ('on_hold', 'En Espera'),
        ('completed', 'Completa'),
        ('cancelled', 'Cancelada'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open', verbose_name='Estado')
    
    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('urgent', 'Urgente'),
    ]
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium', verbose_name='Prioridad')
    
    due_date = models.DateField(blank=True, null=True, verbose_name='Fecha de Vencimiento')
    completed_at = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Completado')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Orden de Trabajo'
        verbose_name_plural = 'Órdenes de Trabajo'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"WO-{self.id.hex[:8]} - {self.title} ({self.asset.name})"
    
    
