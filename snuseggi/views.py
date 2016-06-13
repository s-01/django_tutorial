from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Restaurant
from .models import Assessment
from .models import Menu
from .models import DailyMenu
from .forms import AssessForm
from .forms import AssessForm_sel
from .forms import SelectForm
from django.http import HttpResponse
from django.db.models import Avg
from decimal import *
from tkinter.constants import NUMERIC

import logging
logger = logging.getLogger(__name__)

import pytz
from django.utils import timezone

# Create your views here.
# Create your views here.
def restaurants(request):
    restaurant_list = Restaurant.objects.all()
    for rest in restaurant_list:
        avg_taste = Assessment.objects.filter(restaurant__name=rest.name).aggregate(avg_taste=Avg('point_taste')).get('avg_taste',0.0)
        avg_service = Assessment.objects.filter(restaurant__name=rest.name).aggregate(avg_service=Avg('point_service')).get('avg_service',0.0)
        avg_price = Assessment.objects.filter(restaurant__name=rest.name).aggregate(avg_price=Avg('point_price')).get('avg_price',0.0)
        if(avg_taste == None):
            avg_taste = 0
        if(avg_service == None):
            avg_service = 0
        if(avg_price == None):
            avg_price = 0
        rest.point_taste = avg_taste
        rest.point_service = avg_service
        rest.point_price = avg_price
        rest.point_average = rest.point_avg()
        rest.save()
    restaurant_list.order_by('-point_average')
    return render(request, 'snuseggi/restaurants.html', {'restaurant_list' : restaurant_list})

def assessments(request):
    assessment_list = Assessment.objects.all().order_by('save_time')
    return render(request, 'snuseggi/assessments.html', {'assessment_list' : assessment_list})

def asst_detail(request, pk):
    if request.method == "POST":
        return redirect('/main')
    else:
        asst = get_object_or_404(Assessment, pk=pk)
        return render(request, 'snuseggi/asst_detail.html', {'asst': asst})

def write(request):
    if request.method == "POST":
        form = AssessForm(request.POST, rest = request.POST['restaurant'], clsf = request.POST['classification'], date = request.POST['date'])
        if form.is_valid():
            assess = form.save(commit = False)
            assess.save()
            #form.save()
            #return render(request, 'snuseggi/writeForm.html', {'form': form})
            return redirect('snuseggi.views.asst_detail', pk = assess.pk)
            #return redirect('snuseggi.views.write', {form : 'form'})
    else:
        form = AssessForm_sel()
    return render(request, 'snuseggi/selectForm.html', {'form': form})
