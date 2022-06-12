from django.contrib import admin
from .models import Questions


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'loppis',
        'author',
        'email',
        'content',
        'created_on',
    )
