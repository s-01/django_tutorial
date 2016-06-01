from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.restaurants, name='restaurants'),
    url(r'asst', views.assessments, name='assessments'),
]