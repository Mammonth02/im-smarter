from this import d
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

local_urls = [
    path('shop/', include('apps.shop.urls')),
    path('profile/', include('apps.users.urls')),
    path('site/', include('apps.home_site.urls')),
    path('services/', include('apps.services.urls')),
    path('construction/', include('apps.construction.urls')),
]


api_urls = [
    path('api/site/', include('apps.home_site.API.urls')),
    path('api/shop/', include('apps.shop.API.urls')),
    path('api/users/', include('apps.users.API.urls')),
    path('api/reviews/', include('apps.reviews.API.urls')),
    path('api/services/', include('apps.services.API.urls')),
    path('api/construction/', include('apps.construction.API.urls')),
]

urlpatterns += doc_url
urlpatterns += local_urls + api_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

