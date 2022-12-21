from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.registerAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('user/', views.UserView.as_view()),
    path('logout/', views.LogoutView.as_view())
]