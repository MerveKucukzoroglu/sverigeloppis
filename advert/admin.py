from django.contrib import admin
from .models import Advert


class AdvertAdmin(admin.ModelAdmin):
    readonly_fields = ('ad_number', 'ad_payment_date',)

    fields = ('ad_number', 'ad_payment_date',)

    list_display = ('ad_number', 'ad_payment_date',)

    ordering = ('-ad_payment_date',)


admin.site.register(Advert, AdvertAdmin)
