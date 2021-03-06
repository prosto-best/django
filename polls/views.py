from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! You are here! Here is here!")

# Create your views here.
