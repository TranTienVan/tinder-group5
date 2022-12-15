from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from hello_world.models import Student, Class


def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")
