from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')


def team(request):
    return HttpResponse('team')


def resources(request):
    return HttpResponse('resources')
