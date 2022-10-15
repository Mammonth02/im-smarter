from rest_framework import generics
from rest_framework.permissions  import IsAdminUser
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from apps.services.models import Service


from apps.shop.API.views import Pagination
from apps.users.API.permissions import IsOwner, IsOwnerBasket 
from apps.users.API.serializers import *
from apps.users.models import Basket, Order, User
from apps.construction.models import Pool


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

class BasketListAPI(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsOwnerBasket, )

    def get(self, request, *args, **kwargs):
        products = Basket.objects.filter(user_id = self.request.user.id, status = False)
        return Response(BasketUpdateSerializer(products, many=True).data)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        
        products = Basket.objects.filter(user_id = self.request.user.id, status = False)
        
        serializer.validated_data['basket'] = products
        serializer.save()
        Basket.objects.filter(user_id = self.request.user.id, status = False).update(status = True)

class BasketUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketUpdateSerializer
    permission_classes = (IsOwnerBasket, )

class OrderListUserAPI(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = (IsOwnerBasket, )

    def get_queryset(self):
        return Order.objects.filter(user_id = self.request.user.id, active = True, received = False)

class ServiceListUserAPI(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = (IsOwnerBasket, )

    def get_queryset(self):
        return Service.objects.filter(user_id = self.request.user.id, active = True)

class PoolListUserAPI(generics.ListAPIView):
    queryset = Pool.objects.all()
    serializer_class = PoolListSerializer
    permission_classes = (IsOwnerBasket, )

    def get_queryset(self):
        return Pool.objects.filter(user_id = self.request.user.id, active = True)

class UpdateOrder(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = (IsOwnerBasket, )

    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id = self.kwargs['pk'])
        return Response(OrderListSerializer(order).data)

class UpdateService(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceUpdateSerializer
    permission_classes = (IsOwnerBasket, )

    def get(self, request, *args, **kwargs):
        order = Service.objects.get(id = self.kwargs['pk'])
        return Response(ServiceListSerializer(order).data)

class UpdatePool(generics.UpdateAPIView):
    queryset = Pool.objects.all()
    serializer_class = PoolUpdateSerializer
    permission_classes = (IsOwnerBasket, )

    def get(self, request, *args, **kwargs):
        order = Pool.objects.get(id = self.kwargs['pk'])
        return Response(PoolListSerializer(order).data)