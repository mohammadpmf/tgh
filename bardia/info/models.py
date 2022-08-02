from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    food = models.CharField(max_length=100)