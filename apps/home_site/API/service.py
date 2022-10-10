from django_filters import rest_framework as filters

from apps.services.models import Service
from apps.users.models import Order
from apps.construction.models import Pool



class OrdersFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ['user', 'active', 'received']

class ServiceFilter(filters.FilterSet):
    class Meta:
        model = Service
        fields = ['user', 'active']

class PoolFilter(filters.FilterSet):
    class Meta:
        model = Pool
        fields = ['user', 'active']