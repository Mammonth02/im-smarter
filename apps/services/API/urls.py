from django.urls import path, include
from rest_framework import routers

from apps.services.API.views import CreateService, ListServiceTypeAPI, UpdateDeleteServiceTypeAPI

router = routers.SimpleRouter()


urlpatterns = [
    path('list_service_type/', ListServiceTypeAPI.as_view()),
    path('update_delete_service_type/<int:pk>/', UpdateDeleteServiceTypeAPI.as_view()),
    path('create_service/<int:pk>/', CreateService.as_view()),
]