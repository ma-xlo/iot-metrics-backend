from django.urls import path
from . import views

urlpatterns = [
    path('devices/tags/', views.list_device_tags, name='list-device-tags'),
    path('devices/<int:device_id>/tags/', views.detail_device_tags, name='detail-device-tags'),
    path('devices/online/', views.list_online_devices, name='list-online-devices'),
]