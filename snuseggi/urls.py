from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.restaurants, name='restaurants'),
    url(r'^asst$', views.assessments, name='assessments'),
    url(r'^asst_detail/(?P<pk>[0-9]+)/$', views.asst_detail, name='asst_detail'),
    url(r'^write$', views.write, name='write$'),
]