from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Learn Django for at least 20 minutes every day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Eat no meat for the entire month!',
    'november': 'Walk for at least 20 minutes every day!',
    'december': 'Learn Django for at least 20 minutes every day!',
}

# Create your views here.


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href=\'{month_path}\'>{capitalized_month}</li>'
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    # Get list of months from  monthly_challenges
    months = list(monthly_challenges.keys())

    # Check if specified month number is out of list index range
    if month < 1 or month > len(months):
        return HttpResponseNotFound('Invalid month value specified!')

    # Get month by number
    redirect_month = months[month-1]
    # Dynamically construct url string
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>Invalid month value specified!</h1>')
