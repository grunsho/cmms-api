# Generated by Django 5.2.4 on 2025-07-29 20:51

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Título de la Orden')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('status', models.CharField(choices=[('open', 'Abierta'), ('in_progress', 'En Progreso'), ('on_hold', 'En Espera'), ('completed', 'Completa'), ('cancelled', 'Cancelada')], default='open', max_length=20, verbose_name='Estado')),
                ('priority', models.CharField(choices=[('low', 'Baja'), ('medium', 'Media'), ('high', 'Alta'), ('urgent', 'Urgente')], default='medium', max_length=20, verbose_name='Prioridad')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Vencimiento')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Completado')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to='assets.asset', verbose_name='Activo Asociado')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_work_orders', to=settings.AUTH_USER_MODEL, verbose_name='Asignado a')),
            ],
            options={
                'verbose_name': 'Orden de Trabajo',
                'verbose_name_plural': 'Órdenes de Trabajo',
                'ordering': ['-created_at'],
            },
        ),
    ]
