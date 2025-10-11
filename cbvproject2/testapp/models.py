from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.FloatField()
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    