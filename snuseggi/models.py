from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    rating = models.PositiveSmallIntegerField(default = 0)
    point = models.PositiveSmallIntegerField(default = 0)
    comment = models.TextField()