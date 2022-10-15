from django.urls import path

from apps.home_site.views import *



urlpatterns = [
    path('update_info/<int:pk>', UpdateInfo.as_view(), name='update_info'),
    path('create_info/', CreateInfo.as_view(), name='create_info'),
    path('delete_img/<int:pk>/<int:id>', DeleteImage.as_view(), name='delete_img'),
    path('admin/', Admin.as_view(), name='admin'),
    path('delete_order/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
    path('delete_order_user/<int:pk>/<int:id>/', DeleteOrderUser.as_view(), name='delete_order_user'),
    path('delete_service/<int:pk>/', DeleteService.as_view(), name='delete_service'),
    path('delete_service_user/<int:pk>/<int:id>/', DeleteServiceUser.as_view(), name='delete_service_user'),
    path('delete_pool/<int:pk>/', DeletePool.as_view(), name='delete_pool'),
    path('delete_pool_user/<int:pk>/<int:id>/', DeletePoolUser.as_view(), name='delete_pool_user'),
    path('filter_admin/<slug:s>/', FilterOrders.as_view(), name='filter_admin'),


]