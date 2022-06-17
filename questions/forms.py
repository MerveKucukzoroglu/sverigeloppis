"""Forms file for questions"""
from .models import Questions
from django import forms


class QuestionForm(forms.ModelForm):
    """comment form"""
    class Meta:
        model = Questions
        fields = ('content',)


    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Question"
