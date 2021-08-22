from django.shortcuts import render, redirect
from datetime import date
from .models import Game, Player, Table
# Create your views here.

def home(request):
    games=Game.objects.all()
    return render(request, 'home.html',{'games':games})

def table(request):
    tables=Table.objects.order_by('-team_point')
    return render(request, 'table.html',{'tables':tables})

def stats(request):
    stats=Player.objects.order_by('-player_goals')
    return render(request, 'stats.html',{'stats':stats})

def players(request):
    players=Player.objects.all().order_by('player_name')
    return render(request, 'players.html',{'players':players})

