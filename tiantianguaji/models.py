from django.db import models

# Create your models here.

class player(models.Model):
    userid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    hp = models.FloatField()
    power = models.FloatField()

class clear(models.Model):
    userid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    hp = models.FloatField()
    power = models.FloatField()