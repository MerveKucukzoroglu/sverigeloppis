""" Loppis App urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_loppises, name='loppises'),
    path('<int:loppis_id>/', views.loppis_detail, name='loppis_detail'),
    path('add/', views.add_loppis, name='add_loppis'),
]
