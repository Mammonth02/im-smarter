from rest_framework import serializers

from apps.construction.models import Additionally, Decoration, Pool, PoolCat

class PoolCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolCat
        fields = "__all__"

class AdditionallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionally
        fields = "__all__"

class DecorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoration
        fields = "__all__"

class CreatePoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ['category', 'width', 'length', 'depth', 'decoration', 'additionally', 'desctiption']