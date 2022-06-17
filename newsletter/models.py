from django.db import models


class Newsletter(models.Model):
    """Newsletter modal for signing-up to site newsletter"""
    email = models.EmailField(max_length=254, blank=False, null=False)
    created_on = models.DateTimeField(auto_now=True, editable=False)
