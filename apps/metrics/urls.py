from django.urls import path
from . import views

urlpatterns = [
    path('metrics/', views.list_metrics, name='list-metrics'),
    path('devices/online/', views.list_online_devices, name='list-online-devices'),
]