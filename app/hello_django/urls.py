from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hello_world import views
urlpatterns = [
    path("hello_world/", include("hello_world.urls")),
    path("config/", views.get_publishable_key, name = "config"),
    path("checkout-session", views.get_checkout_session, name = "checkout-session"),
    path("admin/", admin.site.urls)
    
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
