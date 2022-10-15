from django.urls import path, include, re_path
from rest_framework import routers

from apps.users.API.views import *

router = routers.SimpleRouter()


urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('user/<int:pk>/', UserAPI.as_view()),
    
    path('user_for_admin/<int:pk>/', DetailUserAPI.as_view()),
    path('user_list/', UsersListAPI.as_view()),

    path('basket_list/', BasketListAPI.as_view()),
    path('basket_delete_update/<int:pk>/', BasketUpdateDeleteAPI.as_view()),

    path('user_list_order/', OrderListUserAPI.as_view()),
    path('user_list_service/', ServiceListUserAPI.as_view()),
    path('user_list_pool/', PoolListUserAPI.as_view()),

    path('update_order/<int:pk>/', UpdateOrder.as_view()),
    path('update_service/<int:pk>/', UpdateService.as_view()),
    path('update_construction/<int:pk>/', UpdatePool.as_view()),


]