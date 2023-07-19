from django.db import models

class Bar(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    bars = models.ManyToManyField(Bar, related_name='drinks')

    def __str__(self):
        return self.name
    

