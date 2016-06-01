from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    
    def __str__(self):
        return self.name
 
class Restaurant(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    point_taste = models.PositiveSmallIntegerField(default = 0)
    point_service = models.PositiveSmallIntegerField(default = 0)
    point_price = models.PositiveSmallIntegerField(default = 0)

    def point_avg(self):
        return (self.point_taste + self.point_service + self.point_price) / 3

    def __str__(self):
        return self.name
    
class Assessment(models.Model):
    CLASSIFICATION = (('L', 'Lunch'), ('D', 'Dinner'),)
    restuarant = models.ForeignKey('Restaurant')
    classification = models.CharField(max_length=1, choices = CLASSIFICATION, default = 'L')
    menus = models.ManyToManyField(Menu)
    date = models.DateField(auto_now = True)
    point_taste = models.PositiveSmallIntegerField(default = 0)
    point_service = models.PositiveSmallIntegerField(default = 0)
    point_price = models.PositiveSmallIntegerField(default = 0)
    comment = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name