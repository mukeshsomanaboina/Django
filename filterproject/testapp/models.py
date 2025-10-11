from django.db import models

class FilterModel(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    date = models.DateField()