from django.db import models

# Create your models here.
# image,price,name,detail
class Item(models.Model):
    name = models.CharField(max_length=300)
    image = models.TextField()
    price = models.TextField()
    detail = models.TextField(unique=True)