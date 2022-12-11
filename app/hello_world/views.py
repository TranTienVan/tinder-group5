from django.shortcuts import render
from django.contrib.auth import logout 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from hello_world.models import Profile, User
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")



    
class ProfileAPI(APIView):
    def get(self, request, user_id,format = None):
        try: 
            cur_user = User.objects.get(id=user_id)
           
            Profile.objects.get_or_create(user=cur_user)
            cur_user_profile = cur_user.profile
            
            serializer = ProfileSerializer(cur_user_profile)
            return Response(serializer.data)
        except User.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{user_id} Does Not Exist!")

    def put(self, request, user_id):
        try: 
            cur_user = User.objects.get(id=user_id)
            Profile.objects.get_or_create(user=cur_user)
            cur_user_profile = cur_user.profile

            
            cur_user.username = request.POST.get('username')
            cur_user_profile.phone = request.POST.get('phone')
            cur_user_profile.gender = request.POST.get('gender')
            cur_user_profile.is_premium = request.POST.get('is_premium')
            cur_user_profile.about_me = request.POST.get('about_me')
            cur_user_profile.birthday = request.POST.get('birthday')
            cur_user_profile.address = request.POST.get('address')
            cur_user_profile.big_picture_url = request.POST.get('big_picture_url')
            cur_user_profile.small_picture_url = request.POST.get('small_picture_url')
            cur_user_profile.save()
            cur_user.save()


            serializer = ProfileSerializer(cur_user_profile)
            return Response(serializer.data)
        except User.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{user_id} Does Not Exist!")

    def delete(self,request, user_id):
        try: 
            cur_user = User.objects.get(id=user_id)
            Profile.objects.get_or_create(user=cur_user)
            cur_user_profile = cur_user.profile
            logout(request)
            
            cur_user.is_active=False
            cur_user_profile.is_active=False
            return Response(status=status.HTTP_204_NO_CONTENT) 
        except User.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{user_id} Does Not Exist!")
