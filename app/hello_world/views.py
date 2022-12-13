from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from hello_world.models import Student, Class
from hello_world.serializers import ClassSerializer, StudentSerializers


def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")


@csrf_exempt
def classApi(request, id=0):
    if request.method == "GET":
        classes = Class.objects.all()
        classes_serializer = ClassSerializer(classes, many=True)
        
        return JsonResponse(classes_serializer.data, safe=False)
    elif request.method=="POST":
        class_data = JSONParser().parse(request)
        classes_serializer=ClassSerializer(data=class_data)
        
        if classes_serializer.is_valid():
            classes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)    