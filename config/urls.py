from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/e79b4008-b2b6-4e78-8dca-1696b92df35a/', admin.site.urls),
    path('api/v1/', include('apps.metrics.urls')),
    path('api/v1/', include('apps.tags.urls')),
    path('api/v1/', include('apps.devices.urls')),
]
