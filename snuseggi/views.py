from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def restaurants(request):
    restaurant_list = Restaurant.objects.all().order_by('rating')
    return render(request, 'snuseggi/restaurants.html', {'restaurant_list' : restaurant_list})