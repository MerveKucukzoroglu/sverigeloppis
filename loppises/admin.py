""" Loppis Admin """
from django.contrib import admin
from .models import Loppis, County

# Register your models here.

admin.site.register(Loppis)
admin.site.register(County)
