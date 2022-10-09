from django.urls import path
from apps.users.views import *




urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('update_profile/<int:pk>', UpdateProfile.as_view(), name='update_profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('basket/', BasketViewList.as_view(), name='basket'),
    path('list_users/', ListUsers.as_view(), name='list_users'),
    path('detail_user/<int:id>/', DetailUser.as_view(), name='detail_user'),
    path('search_user/', SearchUser.as_view(), name='search_user'),


]