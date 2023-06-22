from django.db import models


class PlayerMinute(models.Model):
    season = models.CharField(max_length=10)
    player_name = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    league = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    club_id = models.IntegerField()
    matches_played_league = models.IntegerField()
    matches_played_competition = models.IntegerField()
    starts_league = models.IntegerField()
    start_competition = models.IntegerField()
    minutes_league = models.IntegerField()
    minutes_competition = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_name


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)
