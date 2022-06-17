"""Forms file for questions"""
from .models import Newsletter
from django import forms


class NewsletterForm(forms.ModelForm):
    """comment form"""
    class Meta:
        model = Newsletter
        fields = ('email', 'created_on',)
