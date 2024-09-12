from collections import defaultdict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Max
from apps.core.models import Metrics, TagDevice
from .serializers import MetricsSerializer
from django.utils import timezone
from datetime import timedelta

@api_view(['GET'])
def list_metrics(request):
    # Calculate the time 60 minutes ago from now
    time_threshold = timezone.now() - timedelta(minutes=420)

    if request.method == 'GET':
        # metrics = Metrics.objects.all()
        metrics = Metrics.objects.filter(timestamp__gte=time_threshold)
        serializer = MetricsSerializer(metrics, many=True)
        serialized_data = serializer.data

        data_by_device = defaultdict(list)
        for item in serialized_data:
            device_id = item.pop('deviceid')
            data_by_device[device_id].append(item)

        device_ids = list(data_by_device.keys())
        tag_devices = TagDevice.objects.filter(device_id__in=device_ids)

        tags_by_device = defaultdict(list)
        for tag_device in tag_devices:
            tags_by_device[tag_device.device_id].append(tag_device.tag_id)

        result = [
            {
                "device": device_id,
                "data": data,
                "tags": tags_by_device[device_id]  
            }
            for device_id, data in data_by_device.items()
        ]

        return Response(result, status=status.HTTP_200_OK)
    return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(['GET'])
# def list_metrics(request):
#   # Calculate the time 10 minutes ago from now
#   time_threshold = timezone.now() - timedelta(minutes=60)

#   if request.method == 'GET':
#     metrics = Metrics.objects.all()
#     # metrics = Metrics.objects.filter(timestamp__gte=time_threshold)
#     serializer = MetricsSerializer(metrics, many=True)
#     serialized_data = serializer.data

#     data_by_device = defaultdict(list)
#     for item in serialized_data:
#       device_id = item.pop('deviceid')  
#       data_by_device[device_id].append(item)

    
#     result = [{"device": device_id, "data": data, "tag": ["ambev", "budweiser"]} for device_id, data in data_by_device.items()]
#     return Response(result, status=status.HTTP_200_OK)
#   return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

