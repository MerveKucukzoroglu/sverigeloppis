"""Profiles app urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('my_loppises/', views.my_loppises, name='my_loppises'),
]
