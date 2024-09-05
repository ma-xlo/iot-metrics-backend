from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.core.models import TagDevice, Tags, Metrics
from django.db.models import Max
from .serializers import TagDeviceSerializer
from apps.tags.serializers import TagsSerializer
from django.utils import timezone
from datetime import timedelta
from django.db import connection

@api_view(['GET', 'POST'])
def list_device_tags(request, device_id):
  if request.method == 'POST':
    tag_name = request.data.get('tag')

    new_tag, created = Tags.objects.get_or_create(name=tag_name)
    device_tag, created = TagDevice.objects.get_or_create(tag_id=new_tag.id, device_id=device_id)

    serializer = TagDeviceSerializer(device_tag)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
  if request.method == 'GET':
    device_tag = TagDevice.objects.filter(device_id=device_id)
    if not device_tag.exists():
      return Response([], status=status.HTTP_404_NOT_FOUND)
    
    serializer = TagDeviceSerializer(device_tag, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'DELETE'])
def detail_device_tags(request, device_id, tag_id):
  if request.method == 'DELETE':
    device_tag = TagDevice.objects.filter(device_id=device_id, tag_id=tag_id)
    device_tag.delete()
    return Response({"message": "ok"}, status=status.HTTP_200_OK)  
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(['GET'])
# def list_online_devices(request):
#     latest_entries = (
#         Metrics.objects.all() 
#         .values('deviceid')
#         .annotate(latest_timestamp=Max('timestamp'))
#     )
#     result = [{"device_id": entry['deviceid'], "timestamp": entry['latest_timestamp']} for entry in latest_entries]
#     return Response(result, status=status.HTTP_200_OK)  