from unicodedata import category
from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)
    site = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    category = models.CharField(max_length=30)


