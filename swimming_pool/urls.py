from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

local_urls = [
    path('site/', include('apps.home_site.urls')),
    path('shop/', include('apps.shop.urls')),
    path('profile/', include('apps.users.urls')),
    path('construction/', include('apps.construction.urls')),
    path('services/', include('apps.services.urls')),
]

urlpatterns += local_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

