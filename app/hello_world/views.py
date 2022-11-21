from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")
