from django.urls import path
from apps.users.views import *




urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    
]