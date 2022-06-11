""" Advert App urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.advert, name='advert'),
    path('advert_success/', views.advert_success, name='advert_success'),
]
