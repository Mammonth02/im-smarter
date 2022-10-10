from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from apps.home_site.API.serializers import ConstructionImagesSerializer, OrderSerializer, PoolSerializer, ServiceSerializer, SiteInfoSerializer
from apps.home_site.API.service import OrdersFilter, PoolFilter, ServiceFilter
from apps.home_site.models import ConstructionImages, SiteInfo
from apps.services.models import Service
from apps.shop.API.permissions import IsAdminOrReadOnly
from apps.users.models import Order
from apps.construction.models import Pool



class UpdateSiteInfoAPI(generics.RetrieveUpdateAPIView):
    queryset = SiteInfo.objects.all()
    serializer_class = SiteInfoSerializer
    permission_classes = (IsAdminOrReadOnly,)

class OrdersAPI(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrdersFilter

class OrderAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)

class ServicesAPI(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ServiceFilter

class ServiceAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUser,)

class PoolsAPI(generics.ListAPIView):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PoolFilter

class PoolAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
    permission_classes = (IsAdminUser,)

class ListCreateConstructionImagesAPI(generics.ListCreateAPIView):
    queryset = ConstructionImages.objects.all()
    serializer_class = ConstructionImagesSerializer
    permission_classes = (IsAdminOrReadOnly,)

class UpdateDeleteConstructionImagesAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConstructionImages.objects.all()
    serializer_class = ConstructionImagesSerializer
    permission_classes = (IsAdminOrReadOnly,)

    