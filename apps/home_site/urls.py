from django.urls import path

from apps.home_site.views import *



urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('update_info/<int:pk>', UpdateInfo.as_view(), name='update_info'),
    path('delete_img/<int:pk>/<int:id>', DeleteImage.as_view(), name='delete_img'),
    path('admin', Admin.as_view(), name='admin'),
    path('create_product', CreateProduct.as_view(), name='create_product'),
    path('create_cat_product', CreateCatProduct.as_view(), name='create_cat_product'),
    path('create_cat_pool', CreateTypePool.as_view(), name='create_cat_pool'),
    path('create_pool_additionally', CreatePoolAdditionally.as_view(), name='create_pool_additionally'),
    path('create_pool_decoration', CreatePoolDecoration.as_view(), name='create_pool_decoration'),
    path('create_service_type', CreateServiceType.as_view(), name='create_service_type'),

]