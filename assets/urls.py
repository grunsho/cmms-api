from rest_framework.routers import DefaultRouter
from .views import AssetViewSet

router = DefaultRouter()
router.register(r'assets', AssetViewSet) # Registra el ViewSet para la ruta 'assets'

urlpatterns = router.urls