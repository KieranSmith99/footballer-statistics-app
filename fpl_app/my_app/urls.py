from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fpl-home'), # After this is loaded, at the empty path, we load views.home.
]