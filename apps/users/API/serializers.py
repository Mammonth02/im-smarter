from rest_framework import serializers

from apps.users.models import User

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'phone', 'address')

class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'