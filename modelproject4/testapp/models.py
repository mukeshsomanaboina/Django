from django.db import models

class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()

class BanJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()
                      
class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()