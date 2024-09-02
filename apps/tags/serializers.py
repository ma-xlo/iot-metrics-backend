from rest_framework import serializers
from apps.core.models import Tags

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
       





