from django.db import models

# Create your models here.
class Skiils(models.Model):
    title = models.CharField(max_length=150)
    persent = models.IntegerField(max_length=3)