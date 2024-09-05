from django.urls import path
from . import views

urlpatterns = [
    # Devices
    # path('devices/', views.list_devices, name='detail-device-tags'),
    # path('devices/online/', views.list_online_devices, name='list-online-devices'),
    
    # Device Tags
    path('devices/<str:device_id>/tags/', views.list_device_tags, name='list-device-tags'),
    path('devices/<str:device_id>/tags/<int:tag_id>', views.detail_device_tags, name='detail-device-tags'),
]