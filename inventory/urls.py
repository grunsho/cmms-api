from rest_framework.routers import DefaultRouter
from .views import PartViewSet

router = DefaultRouter()
router.register(r'parts', PartViewSet) # Registra el Viewset para la ruta 'parts'

urlpatterns = router.urls