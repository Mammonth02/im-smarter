from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from apps.reviews.API.permissions import IsOwnerOrAdmin
from apps.reviews.API.serializers import ReviewsCreateSerializer, ReviewsListSerializer
from apps.reviews.models import Reviews


class ListCreateReviewsAPI(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        rev = Reviews.objects.filter(product_id = self.kwargs['pk'])

        return Response(ReviewsListSerializer(rev, many=True).data)
    
    def perform_create(self, serializer):
        serializer.validated_data['product_id'] = self.kwargs['pk']
        serializer.validated_data['user'] = self.request.user
        serializer.save()

class DeleteReviewsAPI(generics.RetrieveDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsListSerializer
    permission_classes = (IsOwnerOrAdmin, )