"""Newsletter Subscription App"""
from django.apps import AppConfig


class SubscriptionConfig(AppConfig):
    """Subscription appconfig"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscription'
