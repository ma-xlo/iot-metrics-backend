from collections import defaultdict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import OuterRef, Subquery
from apps.core.models import Metrics, TagDevice
from .serializers import MetricsSerializer
from django.utils import timezone
from datetime import timedelta
from apps.core.helpers import is_device_online
from django.db import connection
import json

@api_view(['GET'])
def list_metrics(request):
    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                cursor.execute('CALL GetMetrics()')
                results = cursor.fetchall()
                
                # Process the results to convert to JSON
                processed_results = []
                for row in results:
                    device_id, data_json, tags_json = row
                    data = json.loads(data_json)  # Convert JSON string to Python list
                    tags = json.loads(tags_json)  # Convert JSON string to Python list
                    processed_results.append({
                        "id": device_id,
                        "data": data,
                        "online": is_device_online(data),
                        "tags": tags
                    })
                
                return Response(processed_results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

