from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Don't eat meat for entire month",
    "february": "Practice coding for 10 hours everyday",
    "march": "Learn Django for 30 min every day",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes everyday!",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at 20 minutes every day",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at 20 minutes every day",
    "december": "Learn Django for at least 20 minutes every day"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_txt = monthly_challenges[month]
        return HttpResponse(challenge_txt)
    except:
        return HttpResponseNotFound("This month is not Found")
    