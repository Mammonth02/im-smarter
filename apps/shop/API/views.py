from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


from apps.shop.API.permissions import IsAdminOrReadOnly
from apps.shop.API.serializers import ListImagesProductSerializer, ProductSerializer
from apps.shop.API.service import ProductFilter
from apps.shop.models import ImagesForProducts, Product


class Pagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ListCreateProductsAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = Pagination

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['price']

class UpdateDeleteSingleProductAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)

class ListImagesProductAPI(generics.ListCreateAPIView):
    queryset = ImagesForProducts.objects.all()
    serializer_class = ListImagesProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return ImagesForProducts.objects.filter(product_id = self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.validated_data['product_id'] = self.kwargs['pk']
        return super().perform_create(serializer)

class DeleteImagesProductAPI(generics.RetrieveDestroyAPIView):
    queryset = ImagesForProducts.objects.all()
    serializer_class = ListImagesProductSerializer
    permission_classes = (IsAdminUser,)