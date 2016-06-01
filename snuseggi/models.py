from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    rating = models.PositiveSmallIntegerField(default = 0)
    point_taste = models.PositiveSmallIntegerField(default = 0)
    point_service = models.PositiveSmallIntegerField(default = 0)
    point_price = models.PositiveSmallIntegerField(default = 0)
    comment = models.TextField()
    
    def point_avg(self):
        return (self.point_taste + self.point_service + self.point_price) / 3
    
class Assessment(models.Model):
    restuarant = models.ForeignKey('Restaurant')
    date = models.DateField(auto_now = True)
    point_taste = models.PositiveSmallIntegerField(default = 0)
    point_service = models.PositiveSmallIntegerField(default = 0)
    point_price = models.PositiveSmallIntegerField(default = 0)
    comment = models.CharField(max_length = 200)