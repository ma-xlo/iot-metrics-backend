from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.core.models import TagDevice, Tags, Metrics
from django.db.models import Max
from .serializers import TagDeviceSerializer
from apps.metrics.serializers import MetricsSerializer
from apps.tags.serializers import TagsSerializer
from django.utils import timezone
from datetime import timedelta
from django.db import connection
from apps.core.helpers import is_device_online
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_device_metrics(request, device_id):

  if request.method == 'GET':
      metrics = Metrics.objects.filter(deviceid=device_id)
      serializer = MetricsSerializer(metrics, many=True)
      serialized_data = serializer.data

      device_tags = TagDevice.objects.filter(device_id__in=device_id)

      device_data = {
        "id": device_id,
        "data": serialized_data,
        "online": is_device_online(serialized_data),
        "tags": device_tags
      }

      return Response(device_data, status=status.HTTP_200_OK)
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def list_device_tags(request, device_id):
  if request.method == 'POST':
    new_tag = request.data.get('tag')

    tag, created = Tags.objects.get_or_create(name=new_tag)
    device_tag, created = TagDevice.objects.get_or_create(tag_id=tag.id, device_id=device_id)

    serializer = TagDeviceSerializer(device_tag)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
  if request.method == 'GET':
    device_tags = TagDevice.objects.filter(device_id=device_id)
    
    if not device_tags.exists():
      return Response([], status=status.HTTP_404_NOT_FOUND)
    

    serializer = TagDeviceSerializer(device_tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'DELETE'])
def detail_device_tags(request, device_id, tag_id):
  if request.method == 'DELETE':
    device_tag = TagDevice.objects.filter(device_id=device_id, tag_id=tag_id)
    device_tag.delete()
    return Response({"message": "ok"}, status=status.HTTP_200_OK)  
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@api_view(['POST'])
def send_command(request, device_id):
    try:
        command = request.data.get("command")
        if not command:
            return Response({"error": "No command provided"}, status=400)

        channel_layer = get_channel_layer()

        if channel_layer is None:
            return Response({"error": "Channel layer is None"}, status=500)

        async_to_sync(channel_layer.group_send)(
            f"device_{device_id}",
            {
                'type': 'send_command',
                'message': command
            }
        )

        # response = async_to_sync(channel_layer.receive)(f"device_{device_id}")
        # result = response.get("response", "No response from device")
        # return Response({"message": response}, status=200)

        return Response({"message": f"Command result: ok"}, status=200)

    except Exception as e:
        return Response({"error": str(e)}, status=500)