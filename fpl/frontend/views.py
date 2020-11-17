from django.shortcuts import render
from . import main

# Create your views here.

def home(request):
    return render(request, 'frontend/home.html')

def value(request):
    valueResult = main.high_value_players()
    return render(request, 'frontend/value.html', {'high_value_players': valueResult})

def club_value(request):
    return render(request, 'frontend/club_value.html')

def points(request):
    return render(request, 'frontend/points.html')

def player_search(request):
    return render(request, 'frontend/player_search.html')
