from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse

def home(request):
    return render(request, 'links/home.html')


def team(request):
    return render(request, 'links/team.html')


def resources(request):
    return HttpResponse('resources')
