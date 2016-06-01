from django.shortcuts import render
from .models import Restaurant
from .models import Assessment

# Create your views here.
def restaurants(request):
    restaurant_list = Restaurant.objects.all().order_by('rating')
    return render(request, 'snuseggi/restaurants.html', {'restaurant_list' : restaurant_list})

def assessments(request):
    assessment_list = Assessment.objects.all().order_by('date')
    return render(request, 'snuseggi/assessments.html', {'assessment_list' : assessment_list})