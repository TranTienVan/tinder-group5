from django.urls import path
from .views import hello_world, MembersInforAPI, MembersSettingsAPI

urlpatterns = [
    path("", hello_world, name="hello"),
    path('users', MembersInforAPI.as_view(), name = "setup_profile"),
    path('settings', MembersSettingsAPI.as_view(), name = "setup_settings"),
]

