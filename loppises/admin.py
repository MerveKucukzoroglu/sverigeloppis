""" Loppis Admin """
from django.contrib import admin
from .models import Loppis, County

# Register your models here.


class LoppisAdmin(admin.ModelAdmin):
    """Loppis Admin"""
    list_display = (
        'seller',
        'county',
        'country',
        'created_on',
        'start_date',
        'end_date',
    )

    ordering = ('created_on',)


class CountyAdmin(admin.ModelAdmin):
    """County Admin"""
    list_display = (
        'friendly_name',
        'county',
    )


admin.site.register(Loppis, LoppisAdmin)
admin.site.register(County, CountyAdmin)
