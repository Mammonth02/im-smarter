from django.urls import path

from .views import *




urlpatterns = [
    path('construction/', cListView.as_view(), name='construction'),
    path('create_cat_pool', CreateTypePool.as_view(), name='create_cat_pool'),
    path('create_pool_additionally', CreatePoolAdditionally.as_view(), name='create_pool_additionally'),
    path('create_pool_decoration', CreatePoolDecoration.as_view(), name='create_pool_decoration'),

    path('list_pool_cats/', ListTypesPoolView.as_view(), name='list_pool_cats'),
    path('update_cat_pool/<int:pk>/', UpdateCategoryPool.as_view(), name='update_cat_pool'),
    path('delete_cat_pool/<int:pk>/', DeleteCategoryPool.as_view(), name='delete_cat_pool'),

    path('list_decorations/', ListDecorationView.as_view(), name='list_decorations'),
    path('update_decoration/<int:pk>/', UpdateDecoration.as_view(), name='update_decoration'),
    path('delete_decoration/<int:pk>/', DeleteDecoration.as_view(), name='delete_decoration'),

    path('list_additionally/', ListAdditionallyView.as_view(), name='list_additionally'),
    path('update_additionally/<int:pk>/', UpdateAdditionally.as_view(), name='update_additionally'),
    path('delete_additionally/<int:pk>/', DeleteAdditionally.as_view(), name='delete_additionally'),

]