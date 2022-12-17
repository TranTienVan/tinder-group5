from django.urls import path
from .views import hello_world, MembersInforAPI, MembersSettingsAPI

urlpatterns = [
    path("", hello_world, name="hello"),
    path('users/<int:id>', MembersInforAPI.as_view(), name = "setup_profile"),
    path('settings/<int:user_id>', MembersSettingsAPI.as_view(), name = "setup_settings"),
]

