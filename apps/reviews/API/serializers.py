from rest_framework import serializers

from apps.reviews.models import Reviews

class ReviewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'rating', "text", "time_c", 'user']

class ReviewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['rating', "text",]