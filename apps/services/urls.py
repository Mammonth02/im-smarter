from .views import *
from django.urls import path
from apps.shop.views import *




urlpatterns = [
    path('services/', ServicesListView.as_view(), name='services'),
    path('service/<int:id>/', ServiceView.as_view(), name='service'),


]