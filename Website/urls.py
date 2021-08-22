from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 path("", views.home, name="home"),
 path("home", views.home, name="home"),
 path("table", views.table, name="table"),
 path("players", views.players, name="players"),
 path("stats", views.stats, name="stats"),
 ]
