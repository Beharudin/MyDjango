from django.contrib import admin
from .models import Game, Player, Table

# Register your models here.
admin.site.register(Game),
admin.site.register(Player),
admin.site.register(Table)
