from .views import *
from django.urls import path




urlpatterns = [
    path('service/<int:id>/', ServiceView.as_view(), name='service'),
    
    path('services/', ServicesListView.as_view(), name='services'),
    path('update_service/<int:pk>/', UpdateServiceType.as_view(), name='update_service'),
    path('delete_service_type/<int:pk>/', DeleteServiceType.as_view(), name='delete_service_type'),
    path('create_service_type', CreateServiceType.as_view(), name='create_service_type'),

]