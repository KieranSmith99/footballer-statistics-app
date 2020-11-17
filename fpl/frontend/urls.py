from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('value/', views.value, name="value"),
    path('points/', views.points, name="points"),
    path('playersearch/', views.player_search, name="player-search"),
    path('clubvalue/', views.club_value, name="club-value"),
]