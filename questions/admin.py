"""Questions Admin File"""
from django.contrib import admin
from .models import Questions


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    """Question Admin"""
    list_display = (
        'loppis',
        'author',
        'email',
        'content',
        'created_on',
    )
