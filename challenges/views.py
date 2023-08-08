from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Don't eat meat for entire month")

def february(request):
    return HttpResponse("Practice coding for 10 hours everyday")
