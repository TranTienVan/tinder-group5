from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("hello_world/", include("hello_world.urls")),
    path("admin/", admin.site.urls),
    path("", include("tinder.urls"))
    
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
