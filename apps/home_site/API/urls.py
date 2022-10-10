from django.urls import path, include
from rest_framework import routers

from apps.home_site.API.views import *

router = routers.SimpleRouter()


urlpatterns = [
    path('update_site_info/<int:pk>/', UpdateSiteInfoAPI.as_view()),

    path('orders/', OrdersAPI.as_view()),
    path('order/<int:pk>/', OrderAPI.as_view()),

    path('services/', ServicesAPI.as_view()),
    path('service/<int:pk>/', ServiceAPI.as_view()),

    path('pools/', PoolsAPI.as_view()),
    path('pool/<int:pk>/', PoolAPI.as_view()),

    path('list_create_construction_images/', ListCreateConstructionImagesAPI.as_view()),
    path('update_delete_construction_images/<int:pk>/', UpdateDeleteConstructionImagesAPI.as_view()),


]