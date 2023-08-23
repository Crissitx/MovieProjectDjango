from django.db import models
from django.contrib import admin

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="movie/images")
    url = models.URLField(blank=True)
class Premieres(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="premiere/images")