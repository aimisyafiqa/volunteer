from django.db import models

# Create your models here.
class Student(models.Model):
    studentid = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=100)
    studentname = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class Event (models.Model):
    eventid= models.CharField (max_length=4, primary_key=True)
    eventname = models.TextField()
    place = models.TextField()
    date=models.DateField()
    time = models.TimeField()

class Volunteer (models.Model):
    volunteerid= models.AutoField( primary_key=True, default=None)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    eventid= models.ForeignKey(Event, on_delete=models.CASCADE)