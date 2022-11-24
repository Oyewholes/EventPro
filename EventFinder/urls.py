# EventFinder urls.py file
from django.urls import re_path, path
from . import views


app_name = 'EventFinder'

urlpatterns = [
    re_path(r'^finder$', views.EventFinder.as_view(), name='finder'),
    path('events/<int:event_id>/register/', views.RegistrationPage.as_view(), name='registration'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='detail'),
]