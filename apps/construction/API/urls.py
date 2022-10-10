from django.urls import path, include
from rest_framework import routers

from apps.construction.API.views import *


urlpatterns = [
    path('create_list_pool_type/', ListCreatePoolTypeAPI.as_view()),
    path('update_delete_pool_type/<int:pk>', UpdateDeletePoolTypeAPI.as_view()),

    path('create_list_pool_additionally/', ListCreatePoolAdditionallyAPI.as_view()),
    path('update_delete_pool_additionally/<int:pk>', DeleteUpdatePoolAdditionallyAPI.as_view()),
    
    path('create_list_pool_decoration/', ListCreatePoolDecorationAPI.as_view()),
    path('update_delete_pool_decoration/<int:pk>', DeleteUpdatePoolDecorationAPI.as_view()),

    path('create_pool/', CreatePoolAPI.as_view()),

]