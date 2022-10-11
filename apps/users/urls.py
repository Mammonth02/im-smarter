from django.urls import path
from apps.users.views import *




urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('update_profile/<int:pk>', UpdateProfile.as_view(), name='update_profile'),
    path('login/', LoginView.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('basket/', BasketViewList.as_view(), name='basket'),
    path('list_users/', ListUsers.as_view(), name='list_users'),
    path('detail_user/<int:id>/', DetailUser.as_view(), name='detail_user'),
    path('detail_user_for_user/<int:id>/', DetailUserForUser    .as_view(), name='detail_user_for_user'),
    path('search_user/', SearchUser.as_view(), name='search_user'),

]