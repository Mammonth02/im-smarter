from rest_framework import serializers

from apps.home_site.models import ConstructionImages, SiteInfo
from apps.services.models import Service
from apps.users.models import Order
from apps.construction.models import Pool


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = "__all__"

class ConstructionImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionImages
        fields = "__all__"