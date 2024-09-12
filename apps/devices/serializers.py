from rest_framework import serializers
from apps.core.models import TagDevice, Tags

class TagDeviceSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = TagDevice
        fields = ['device_id', 'tag_id', 'name']

    def get_name(self, obj):
        tag = Tags.objects.get(id=obj.tag_id)
        return tag.name




