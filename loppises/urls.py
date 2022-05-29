""" Loppis App urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_loppises, name='loppises'),
    path('<loppis_id>', views.loppis_detail, name='loppis_detail'),
]
