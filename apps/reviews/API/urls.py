from django.urls import path, include
from rest_framework import routers

from apps.reviews.API.views import DeleteReviewsAPI, ListCreateReviewsAPI

router = routers.SimpleRouter()


urlpatterns = [
    path('list_or_create_reviews/<int:pk>/', ListCreateReviewsAPI.as_view()),
    path('delete_reviews/<int:pk>/', DeleteReviewsAPI.as_view()),

]