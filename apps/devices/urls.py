from django.urls import path
from . import views

urlpatterns = [
    # Devices
    # path('devices/command/', views.send_command, name='send-command'),
    path('devices/<str:device_id>/command/', views.send_command),

    path('devices/<str:device_id>/', views.list_device_metrics, name='list-device-metrics'),
    # path('devices/', views.list_devices, name='detail-device-tags'),
    
    # Device Tags
    path('devices/<str:device_id>/tags/', views.list_device_tags, name='list-device-tags'),
    path('devices/<str:device_id>/tags/<int:tag_id>', views.detail_device_tags, name='detail-device-tags'),
]