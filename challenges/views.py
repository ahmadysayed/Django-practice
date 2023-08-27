from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_txt = monthly_challenges[month]
        response_data = f"<h1>{challenge_txt}</h1>"
        return HttpResponse(response_data)
    except: 
        return HttpResponseNotFound("<h1>This month is not Found</h1>")
    