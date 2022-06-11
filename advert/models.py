import uuid
from django.db import models


class Advert(models.Model):
    """Advertisement model"""
    ad_number = models.CharField(max_length=32, null=False, editable=False)
    ad_payment_date = models.DateTimeField(auto_now_add=True)

    def _generate_ad_number(self):
        """ Generate random unique ad number using UUID """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override the original save method
        to set the ad number if it hasn't been already set."""
        if not self.ad_number:
            self.ad_number = self._generate_ad_number()
        super().save(*args, *kwargs)

    def __str__(self):
        return self.ad_number
