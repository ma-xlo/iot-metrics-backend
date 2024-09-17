# from django.urls import path
# from apps.devices.consumers import RaspberryConsumer

# websocket_urlpatterns = [
#     path('ws/raspberry/', RaspberryConsumer.as_asgi()),
# ]

from django.urls import re_path
from apps.devices.consumers import RaspberryConsumer

websocket_urlpatterns = [
    re_path(r'ws/device/(?P<device_id>\w+)/$', RaspberryConsumer.as_asgi()),
]