from rest_framework import serializers

from apps.shop.models import Category, ImagesForProducts, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ListImagesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesForProducts
        fields = ['id', "image"]

class CatProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'parent']
