from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyUserSerializer
from .models import MyUser
from rest_framework.exceptions import AuthenticationFailed
from .handlers import JWTHandler
import jwt
import os 

JWT_COOKIE = os.environ.get("JWT_COOKIE")

class registerAPIView(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)   #if anything not valid, raise exception
        serializer.save()
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        #find user using email
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

        #if password correct
        return response


# get user using cookie
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get(JWT_COOKIE)

        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        
        try:
            id = JWTHandler.verify_token(token)
            #decode gets the user

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        
        user = MyUser.objects.filter(id = id).first()
        serializer = MyUserSerializer(user)

        return Response(serializer.data)
        #cookies accessed if preserved

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(JWT_COOKIE)
        response.data = {
            'message': 'successful'
        }

        return response