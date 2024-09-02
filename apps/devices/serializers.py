from rest_framework import serializers
from apps.core.models import TagDevice

class TagDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDevice
        fields = '__all__'
       





