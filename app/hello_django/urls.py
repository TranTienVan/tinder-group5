from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from tinder_profile import views
    
from django.views.generic import RedirectView, TemplateView



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('authentication.urls')),
    path("api/", include("tinder.urls")),
    path("api/", include("tinder_profile.urls")),

    # JUST FOR AUTO PROCESS
    path("config/", views.get_publishable_key, name = "config"),
    path("checkout-session/", views.get_checkout_session, name = "checkout-session"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
