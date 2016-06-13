from django.contrib import admin
from .models import Restaurant
from .models import Assessment
from .models import Menu
from .models import DailyMenu

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Assessment)
admin.site.register(Menu)
admin.site.register(DailyMenu)