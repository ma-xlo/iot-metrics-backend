from collections import defaultdict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.core.models import Metrics
from .serializers import MetricsSerializer
from django.utils import timezone
from datetime import timedelta

@api_view(['GET'])
def list_metrics(request):
  # Calculate the time 10 minutes ago from now
  time_threshold = timezone.now() - timedelta(minutes=10)

  if request.method == 'GET':
    # metrics = Metrics.objects.all()
    metrics = Metrics.objects.filter(timestamp__gte=time_threshold)
    serializer = MetricsSerializer(metrics, many=True)
    serialized_data = serializer.data

    data_by_device = defaultdict(list)
    for item in serialized_data:
      device_id = item.pop('deviceid')  
      data_by_device[device_id].append(item)

    result = [{"device": device_id, "data": data} for device_id, data in data_by_device.items()]
    return Response(result, status=status.HTTP_200_OK)
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def list_online_devices(request):
  time_threshold = timezone.now() - timedelta(minutes=5)
  device_ids = Metrics.objects.filter(timestamp__gte=time_threshold).values_list('deviceid', flat=True).distinct()
  result = [{"deviceid": deviceid} for deviceid in device_ids]
  return Response(result, status=status.HTTP_200_OK)