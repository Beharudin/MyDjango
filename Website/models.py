from django.db import models

# Create your models here.
match_Status = (
    ('HT', 'HT'),
    ('FT', 'FT'),
)

class Game(models.Model):
   team1_name = models.CharField(max_length=50)
   team2_name = models.CharField(max_length=50)
   stadium = models.CharField(max_length=50)
   week_day = models.CharField(max_length=50)
   game_day = models.IntegerField()
   game_month = models.IntegerField()
   game_year = models.IntegerField()
   team1_goals = models.IntegerField()
   team2_goals = models.IntegerField()
   game_no = models.IntegerField(default=1)
   match_status = models.CharField(max_length=20, choices=match_Status, default='FT')
   game_status = models.BooleanField(default=False)


class Player(models.Model):
   player_name = models.CharField(max_length=50)
   player_team = models.CharField(max_length=50)
   player_no = models.IntegerField()
   player_goals = models.IntegerField()


class Table(models.Model):
   team_name = models.CharField(max_length=50)
   team_played = models.IntegerField()
   team_win = models.IntegerField()
   team_draw = models.IntegerField()
   team_loose = models.IntegerField()
   team_point = models.IntegerField()
   team_goal = models.IntegerField()


