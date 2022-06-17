from django.db import models

class Subscriptions(models.Model):
    """Newsletter subsription model"""
    email = models.EmailField()
    subscribed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['subscribed_on']
        verbose_name_plural = 'Subscriptions'


    def __str__(self):
        return self.email
