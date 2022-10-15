from rest_framework import serializers

from apps.services.models import Service, ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['message']