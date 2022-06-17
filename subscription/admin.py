from django.contrib import admin
from .models import Subscriptions


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'subscribed_on',
    )
