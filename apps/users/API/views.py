from rest_framework import generics, viewsets
from rest_framework.permissions  import IsAdminUser
from rest_framework.filters import SearchFilter

from apps.shop.API.views import Pagination
from apps.users.API.permissions import IsOwner 
from apps.users.API.serializers import DetailUserSerializer, UpdateUserSerializer
from apps.users.models import User


class UserAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsOwner, )

class DetailUserAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = DetailUserSerializer
    permission_classes = (IsAdminUser, )

class UsersListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = DetailUserSerializer
    permission_classes = (IsAdminUser, )
    filter_backends = (SearchFilter,)
    search_fields = ['username']
    pagination_class = Pagination





