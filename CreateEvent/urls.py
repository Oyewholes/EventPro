# CreateEvent urls.py file
from django.urls import re_path
from . import views

app_name = 'CreateEvent'

urlpatterns=[
    re_path(r'^new$', views.CreateEvent.as_view(), name='create'),
    re_path(r'^ticket$', views.AddTickets.as_view(), name='addticket'),
    re_path(r'^dashboard$', views.Dashboard.as_view(), name='dashboard')
]