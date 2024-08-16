from rest_framework import serializers
from apps.core.models import Metrics

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'
       





