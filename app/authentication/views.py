from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyUserSerializer
from .models import MyUser
from rest_framework.exceptions import AuthenticationFailed
from .handlers import JWTHandler
from tinder_profile.models import Members, MembersInfo
import os 
from django.http.request import HttpRequest

JWT_COOKIE = os.environ.get("JWT_COOKIE")

class RegisterAPIView(APIView):
    def post(self, request: HttpRequest, format = None):
        serializer = MyUserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        user = MyUser.objects.filter(id = serializer.data['id']).first()
        member = Members.objects.create(user_id=user.id)
        member.save()
        member_info = MembersInfo.objects.create(user_id = user.id, avatar_url = "uploads/default.jpg")
        member_info.save()
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request, format = None):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email, password)

        user = MyUser.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed('User not found:)')
            
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')

        
        token = JWTHandler.generate_token(user)

        response = Response() 

        response.set_cookie(key = JWT_COOKIE, value = token, httponly = True)  # httonly - frontend can't access cookie, only for backend

        response.data = {
            JWT_COOKIE: token
        }

        return response

class LogoutView(APIView):
    def post(self, request, format = None):
        response = Response()
        response.delete_cookie(JWT_COOKIE)
        response.data = {
            'message': 'successful'
        }

        return response