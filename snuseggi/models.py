from django.db import models
from datetime import datetime

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
POINT_CHOICES = (
                 (ZERO, '0'),
                 (ONE, '1'),
                 (TWO, '2'),
                 (THREE, '3'),
                 (FOUR, '4'),
                 (FIVE, '5'),)

CLASSIFICATION = (('Lunch', 'Lunch'), ('Dinner', 'Dinner'),)

class Menu(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    
    def __str__(self):
        return self.name
    
class Restaurant(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    menus = models.ManyToManyField(Menu, through='DailyMenu')
    point_taste = models.PositiveSmallIntegerField(default = 0, choices = POINT_CHOICES)
    point_service = models.PositiveSmallIntegerField(default = 0, choices = POINT_CHOICES)
    point_price = models.PositiveSmallIntegerField(default = 0, choices = POINT_CHOICES)
    point_average = models.FloatField(default = 0)

    def point_avg(self):
        return (self.point_taste + self.point_service + self.point_price) / 3

    def __str__(self):
        return self.name
    
class DailyMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField(default = datetime.today)
    classification = models.CharField(max_length=6, choices = CLASSIFICATION, default = 'Lunch')
    
    def __str__(self):
        return str(self.date) + " " + self.restaurant.name + " " + self.classification + " " + self.menu.name
    
    def __rst__(self):
        return self.restaurant.pk
    
class Assessment(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=False, null=False, default = '301동')
    classification = models.CharField(max_length=6, choices = CLASSIFICATION, default = 'Lunch')
    date = models.DateField(default = datetime.today)
    dailyMenu = models.ForeignKey(DailyMenu, blank=False, null=False)
    save_time = models.DateTimeField(default = datetime.now)
    point_taste = models.PositiveSmallIntegerField(choices = POINT_CHOICES, blank=False, null=False, default = 5)
    point_service = models.PositiveSmallIntegerField(choices = POINT_CHOICES, blank=False, null=False, default = 5)
    point_price = models.PositiveSmallIntegerField(choices = POINT_CHOICES, blank=False, null=False, default = 5)
    comment = models.CharField(max_length = 200, blank=True, null=True)
    
    def __str__(self):
        return str(self.date) + " " + str(self.save_time)
    

class Select(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=False, null=False, default = '301동')
    classification = models.CharField(max_length=6, choices = CLASSIFICATION, default = 'Lunch')
    date = models.DateField(default = datetime.today)