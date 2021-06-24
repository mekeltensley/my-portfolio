"""Defines URL patterns for portfolio"""

from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.home, name='home'),
]
