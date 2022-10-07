from django.urls import path
from apps.shop.views import *
from apps.reviews.views import DeleteRev




urlpatterns = [
    path('list/<int:id>/', ShopCat.as_view(), name='shop_cat'),
    path('list/filter/<int:id>/', FilterPrice.as_view(), name='filter'),
    path('single_page/<int:id>/', SingleProduct.as_view(), name='single_page'),
    path('update_product/<int:pk>/', UpdateProduct.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('search/<int:id>/', Search.as_view(), name='search'),
    path('delete_img_product/<int:pk>/<int:id>', DeleteImageProduct.as_view(), name='delete_img_product'),
    path('delete_rev/<int:pk>/<int:id>', DeleteRev.as_view(), name='delete_rev'),
    

]