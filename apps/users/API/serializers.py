from rest_framework import serializers

from apps.construction.models import Pool
from apps.services.models import Service
from apps.users.models import Basket, Order, User

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'phone', 'address')

class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_active', 'last_login',  'image', 'phone', 'address']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = []

class BasketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['id', 'product', 'quantity']

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'time_create', 'cancel_order', 'time_update', 'basket']

class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['received', 'cancel_order']

class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['cancel_service']

class PoolUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ['cancel_construction']