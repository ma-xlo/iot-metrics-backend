from collections import defaultdict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.core.models import Tags
from .serializers import TagsSerializer
from django.utils import timezone
from datetime import timedelta

@api_view(['GET'])
def list_tags(request):
  if request.method == 'GET':
    tags = Tags.objects.all()
    serializer = TagsSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def detail_tags(request, id):
  if request.method == 'GET':
    tag = Tags.objects.get(id=id)
    serializer = TagsSerializer(tag)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
