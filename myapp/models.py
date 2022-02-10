from distutils.command.upload import upload
from enum import auto
from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    desc = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='blogimg')
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    desc = models.CharField(max_length=500)