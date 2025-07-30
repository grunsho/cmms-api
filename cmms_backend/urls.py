from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
    
    path('api/v1/admin/', include('authentication.admin_urls')),
    
    path('api/v1/', include('assets.urls')),
    path('api/v1/', include('work_orders.urls')),
    path('api/v1/', include('inventory.urls')),
]