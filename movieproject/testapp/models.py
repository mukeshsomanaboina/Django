from django.db import models

class Movie(models.Model):
    rdate = models.DateField()
    moviename = models.CharField(max_length=100)
    hero = models.CharField(max_length=100)
    heroine = models.CharField(max_length=100)
    rating = models.FloatField()
