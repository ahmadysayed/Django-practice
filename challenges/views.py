from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_txt = None
    if month == "january":
        challenge_txt = "Don't eat meat for entire month"
    elif month == "february":
        challenge_txt = "Practice coding for 10 hours everyday"
    elif month == "march":
        challenge_txt = "Learn Django for 30 min every day"
    else:
        return HttpResponseNotFound("The Month is not Supported")
    return HttpResponse(challenge_txt)