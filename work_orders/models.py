from django.db import models
import uuid
from assets.models import Asset
from authentication.models import User

class WorkOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name='Título de la Orden')
    
