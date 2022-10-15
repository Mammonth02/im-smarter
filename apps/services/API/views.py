from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.services.API.serializers import CreateServiceSerializer, ServiceTypeSerializer
from apps.services.models import Service, ServiceType
from apps.shop.API.permissions import IsAdminOrReadOnly


class ListServiceTypeAPI(generics.ListCreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = (IsAdminOrReadOnly, )

class UpdateDeleteServiceTypeAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = (IsAdminUser, )

class CreateService(generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_classes = (IsAdminUser, )

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        service_type = ServiceType.objects.get(id = pk)
        if request.user.is_staff:
            return Response(ServiceTypeSerializer(service_type).data)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['category_id'] = self.kwargs['pk']
        return super().perform_create(serializer)
