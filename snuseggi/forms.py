from django.forms import ModelForm
from .models import Restaurant
from .models import Assessment
from .models import DailyMenu
from .models import Select

class AssessForm(ModelForm):
    class Meta:
        model = Assessment
        exclude = ['save_time']
        
    def __init__(self, *args, **kwargs):
        rest = kwargs.pop('rest')
        clsf = kwargs.pop('clsf')
        date = kwargs.pop('date')
        super(AssessForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].initial = Restaurant.objects.get(pk = rest)
        self.fields['classification'].initial = clsf
        self.fields['date'].initial = date
        self.fields['dailyMenu'].queryset = DailyMenu.objects.filter(date = date).filter(classification = clsf).filter(restaurant_id = rest)
        
class AssessForm_sel(ModelForm):
    class Meta:
        model = Assessment
        fields = ['restaurant', 'classification', 'date']
        
class SelectForm(ModelForm):
    class Meta:
        model = Select
        fields = '__all__'