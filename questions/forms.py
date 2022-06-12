"""Forms file for questions"""
from .models import Questions
from django import forms
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    """comment form"""
    class Meta:
        model = Questions
        fields = ('content',)
