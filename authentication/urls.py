from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserManagementViewSet

# Creamos un router para las rutas de gestión de usuarios
router = DefaultRouter()
# Registra nuestro UserManagementViewSet.
# Esto creará rutas como /users/, /users/{id}/, etc.
# Djoser ya maneja /users/me/.
router.register(r'users', UserManagementViewSet, basename='users')

urlpatterns = [
    # Incluye las rutas de Djoser para autenticación (login, logout, set_password, me, etc.)
    # Djoser.urls ya incluye el endpoint 'users/me/' que no debe ser gestionado por el admin
    # en el sentido de que un usuario normal puede acceder a su propio perfil.
    path('', include('djoser.urls')), # Esto ya incluye el 'me' y register
    path('', include('djoser.urls.authtoken')),

    # Incluye las rutas para la gestión de usuarios por el administrador
    # Estas rutas se superponen con las de Djoser para '/users/', pero get_permissions
    # en UserManagementViewSet se encarga de diferenciar el acceso.
    path('', include(router.urls)), # Esto añade /users/ y /users/{id}/
]