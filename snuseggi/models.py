from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    point_0 = models.BooleanField()
    point_1 = models.BooleanField()
    point_2 = models.BooleanField()
    point_3 = models.BooleanField()
    point_4 = models.BooleanField()
    comment = models.TextField()