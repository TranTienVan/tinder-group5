from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path("admin", admin.site.urls),
    path('api/', include('authentication.urls')),
    path("api/", include("tinder.urls")),
    path("api/", include("tinder_profile.urls"))
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
