from django.urls import path
from .views import hello_world, ProfileAPI

urlpatterns = [
    path("", hello_world, name="hello"),
    path('<int:user_id>', ProfileAPI.as_view(), name = "setup_profile"),
]

