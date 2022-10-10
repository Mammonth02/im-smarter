from rest_framework import generics
from apps.construction.API.serializers import AdditionallySerializer, CreatePoolSerializer, DecorationSerializer, PoolCatSerializer
from rest_framework.permissions import IsAdminUser


from apps.construction.models import Additionally, Decoration, Pool, PoolCat
from apps.home_site.API.serializers import PoolSerializer


class ListCreatePoolTypeAPI(generics.ListCreateAPIView):
    queryset = PoolCat.objects.all()
    serializer_class = PoolCatSerializer
    permission_classes = (IsAdminUser,)

class UpdateDeletePoolTypeAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = PoolCat.objects.all()
    serializer_class = PoolCatSerializer
    permission_classes = (IsAdminUser,)

class ListCreatePoolAdditionallyAPI(generics.ListCreateAPIView):
    queryset = Additionally.objects.all()
    serializer_class = AdditionallySerializer
    permission_classes = (IsAdminUser,)

class DeleteUpdatePoolAdditionallyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Additionally.objects.all()
    serializer_class = AdditionallySerializer
    permission_classes = (IsAdminUser,)

class ListCreatePoolDecorationAPI(generics.ListCreateAPIView):
    queryset = Decoration.objects.all()
    serializer_class = DecorationSerializer
    permission_classes = (IsAdminUser,)

class DeleteUpdatePoolDecorationAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Decoration.objects.all()
    serializer_class = DecorationSerializer
    permission_classes = (IsAdminUser,)

class CreatePoolAPI(generics.CreateAPIView):
    queryset = Pool.objects.all()
    serializer_class = CreatePoolSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()