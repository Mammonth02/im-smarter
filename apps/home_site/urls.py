from django.urls import path

from apps.home_site.views import *



urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('update_info/<int:pk>', UpdateInfo.as_view(), name='update_info'),
    path('delete_img/<int:pk>/<int:id>', DeleteImage.as_view(), name='delete_img'),
    path('admin/', Admin.as_view(), name='admin'),
    path('create_product', CreateProduct.as_view(), name='create_product'),
    path('create_cat_product', CreateCatProduct.as_view(), name='create_cat_product'),
    path('create_cat_pool', CreateTypePool.as_view(), name='create_cat_pool'),
    path('create_pool_additionally', CreatePoolAdditionally.as_view(), name='create_pool_additionally'),
    path('create_pool_decoration', CreatePoolDecoration.as_view(), name='create_pool_decoration'),
    path('create_service_type', CreateServiceType.as_view(), name='create_service_type'),
    path('delete_order/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
    path('delete_order_user/<int:pk>/<int:id>/', DeleteOrderUser.as_view(), name='delete_order_user'),
    path('delete_service/<int:pk>/', DeleteService.as_view(), name='delete_service'),
    path('delete_service_user/<int:pk>/<int:id>/', DeleteServiceUser.as_view(), name='delete_service_user'),
    path('delete_pool/<int:pk>/', DeletePool.as_view(), name='delete_pool'),
    path('delete_pool_user/<int:pk>/<int:id>/', DeletePoolUser.as_view(), name='delete_pool_user'),
    path('filter_admin/<slug:s>/', FilterOrders.as_view(), name='filter_admin'),


]