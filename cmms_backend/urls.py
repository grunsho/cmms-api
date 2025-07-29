from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs de autenticación de Djoser (login, register, etc.)
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')), # Para autenticación basada en tokens

    path('api/v1/', include('assets.urls')),
    path('api/v1/', include('work_orders.urls'))
]