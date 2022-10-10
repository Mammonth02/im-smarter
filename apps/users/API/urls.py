from django.urls import path, include, re_path
from rest_framework import routers

from apps.users.API.views import DetailUserAPI, UserAPI, UsersListAPI

router = routers.SimpleRouter()


urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    
    path('user/<int:pk>/', UserAPI.as_view()),
    path('user_for_admin/<int:pk>/', DetailUserAPI.as_view()),
    path('user_list/', UsersListAPI.as_view()),
]