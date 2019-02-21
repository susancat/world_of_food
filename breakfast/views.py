from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Start your day the global way!")
