from django.db import models

class ContactInfo1(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
 

class Student1(ContactInfo1):
    marks = models.IntegerField()
    rollno = models.IntegerField()

class Teacher1(ContactInfo1):
    salary = models.FloatField()
    subject = models.CharField(max_length=100)