from rest_framework.routers import DefaultRouter
from .views import WorkOrderViewSet

router = DefaultRouter()
router.register(r'work-orders', WorkOrderViewSet) # Registra el ViewSet para la ruta 'work-orders'

urlpatterns = router.urls