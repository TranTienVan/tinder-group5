from django.shortcuts import render
from django.contrib.auth import logout 
from rest_framework.request import Request
from django.http import HttpResponse, HttpResponseNotFound
from .models import  Members, MembersInfo, MembersSettings
from .serializers import  MembersInfoSerializer, MembersSettingsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import IntegrityError
from authentication.handlers import JWTHandler
from authentication.models import MyUser

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

class MembersInforAPI(APIView):
    def get(self, request):
        try: 
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user = MyUser.objects.filter(id = id).first()
            user_info, created = MembersInfo.objects.get_or_create(user = user.members)
            
            serializer_context = {
                 'request': request,
            }
            serializer = MembersInfoSerializer(user_info, serializer_context)
            if serializer.is_valid():
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")

    def put(self, request):
        try: 
            
            
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user = Members.objects.get(user_id=id)
            if(request.POST.get('user_name') is not None):
                user.user_name = request.POST.get('user_name') 
            user.save()
            
            user_info, created = MembersInfo.objects.get_or_create(user_id = id)
            user_info.address = request.POST.get('address')
            user_info.street = request.POST.get('street')
            user_info.district = request.POST.get('district')
            user_info.city = request.POST.get('city')
            user_info.country = request.POST.get('country')
            user_info.language = request.POST.get('language')
            user_info.hobby = request.POST.get('hobby')
            user_info.company =request.POST.get('company')
            user_info.school = request.POST.get('school')
            user_info.save()

            serializer_context = {
            'request': request,
            }
            
            serializer = MembersInfoSerializer(user_info, serializer_context)
            if serializer.is_valid():
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except Members.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id}Does Not Exist!")
       

    def delete(self,request):
        try:  
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user= Members.objects.get(user_id = id)
            
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 

        except Members.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")

class MembersSettingsAPI(APIView):
    def get(self, request):
        try: 
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user = MyUser.objects.filter(id = id).first()
            user_setting, created = MembersSettings.objects.get_or_create(user = user.members)

            serializer_context = {
                'request': request,
            }
            serializer = MembersSettingsSerializer(user_setting, serializer_context)
            if serializer.is_valid():
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")

    def put(self, request):
        try: 
            id =  JWTHandler.get_current_user(request.COOKIES)
            user_setting, created = MembersSettings.objects.get_or_create(user_id = id)
            user_setting.search_locations = request.POST.get('search_locations')
            user_setting.max_range = request.POST.get('max_range')
            user_setting.min_match_age = request.POST.get('min_match_age')
            user_setting.max_match_age = request.POST.get('max_match_age')
            user_setting.visibility = request.POST.get('visibility')
            
            serializer_context = {
           'request': request,
            }
            serializer = MembersSettingsSerializer(user_setting, serializer_context)
            if serializer.is_valid():
                user_setting.save()
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")