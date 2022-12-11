from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from hello_world.models import Profile, User
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

# @csrf_exempt 
# @api_view(('GET',))
# def profile(request, user_id):
#     try: 
#         cur_user = User.objects.get(id=user_id)
#         cur_user_profile = Profile.objects.get_or_create(user=cur_user)
#         if request.method == 'GET':
#             # template = loader.get_template('get_user_profile.html')
#             context = {
#                 'username': cur_user.username,
#                 'gender': cur_user.profile.gender,
#                 'about_me': cur_user.profile.about_me
#             }
#             print(cur_user_profile.get_username())
            
#             serialize = ProfileSerializer(cur_user_profile)
#             return Response(serialize.data)
#             # return render(request,'get_user_profile.html',context)
#         elif request.method == 'PUT':
#             if(not cur_user.is_anonymous()):
#                 cur_user_profile = cur_user.profile 
#                 cur_user.username = request.POST.get('username')
#                 cur_user_profile.gender = request.POST.get('gender')
#                 cur_user_profile.about_me = request.POST.get('about_me')
#                 cur_user_profile.save()
#                 cur_user.save()
#                 return HttpResponse("<h1>Successfully updated</h1>")
#         elif request.method == 'DELETE':
#             return

#     except User.DoesNotExist:
#         return HttpResponseNotFound(f"User With ID:{user_id} Does Not Exist!")

    
class ProfileAPI(APIView):
    def get(self, request, user_id,format = None):
        try: 
            cur_user = User.objects.get(id=user_id)
            print(cur_user.username)
            Profile.objects.get_or_create(user=cur_user)
            cur_user_profile = cur_user.profile
            print(cur_user_profile.phone)
            serializer = ProfileSerializer(cur_user_profile)
            return Response(serializer.data)
        except User.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{user_id} Does Not Exist!")

