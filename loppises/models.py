""" Loppis model """
from django.db import models
from django.contrib.auth.models import User


class County(models.Model):
    """ List of Counties in Sweden """

    class Meta:
        """Verbose name for counties"""
        verbose_name_plural = 'Counties'

    county = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.county

    def get_friendly_name(self):
        """get friendly name of County"""
        return self.friendly_name


class Loppis(models.Model):
    """ Loppis ad model """

    class Meta:
        """Loppis Meta class"""
        verbose_name_plural = 'Loppises'
        ordering = ['-created_on']

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.ForeignKey(
        'County', null=True, blank=False, on_delete=models.SET_NULL
        )
    city = models.CharField(max_length=40, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.title
