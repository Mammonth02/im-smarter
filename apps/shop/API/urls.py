from django.urls import path, include
from rest_framework import routers

from apps.shop.API.views import *

router = routers.SimpleRouter()


urlpatterns = [
    path('list_or_create_product/', ListCreateProductsAPI.as_view()),
    path('single_product/<int:pk>/', UpdateDeleteSingleProductAPI.as_view()),
    path('product_images/<int:pk>/', ListImagesProductAPI.as_view()),
    path('product_image_del/<int:pk>/', DeleteImagesProductAPI.as_view()),
    path('list_or_create_category/', ListCreateCatProductAPI.as_view()),
    path('update_delete_category/<int:pk>', UpdateDeleteCategory.as_view()),


]