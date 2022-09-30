from .views import *
from django.urls import path
from apps.shop.views import *




urlpatterns = [
    path('construction/', cListView.as_view(), name='construction'),


]