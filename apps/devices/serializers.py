from rest_framework import serializers
from apps.core.models import TagDevice, Tags

class TagDeviceSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = TagDevice
        fields = ['device_id', 'tag_id', 'tag_name']

    def get_tag_name(self, obj):
        tag = Tags.objects.get(id=obj.tag_id)
        return tag.name




