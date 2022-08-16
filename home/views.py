from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Read Operation")

def update(request):
    return HttpResponse("Update Operation")

def delete(request):
    return HttpResponse("Delete Operation")
