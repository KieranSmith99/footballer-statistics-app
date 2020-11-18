from django.shortcuts import render
from . import api

# Create your views here.

def home(request):
    return render(request, 'frontend/home.html')

def value(request):
    valueResult = api.high_value_players()
    return render(request, 'frontend/value.html', {'high_value_players': valueResult})

def club_value(request):
    clubResult = api.most_valuable_teams()
    return render(request, 'frontend/club_value.html', {'most_valuable_teams': clubResult})

def points(request):
    pointsResult = api.highest_points()
    return render(request, 'frontend/points.html', {'highest_points': pointsResult})

def player_search(request):
    return render(request, 'frontend/player_search.html')
