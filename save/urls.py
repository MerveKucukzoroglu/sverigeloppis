""" Save App urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_save, name='view_save'),
]
