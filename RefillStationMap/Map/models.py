from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    site = models.TextField(unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    category = models.TextField() #카테고리도 여러종류일 수 있음
    sub_category = models.TextField()


