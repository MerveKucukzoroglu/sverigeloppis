"""Forms file for questions"""
from django import forms
from .models import Questions


class QuestionForm(forms.ModelForm):
    """question form"""
    class Meta:
        """Question Form Meta class"""
        model = Questions
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Question"
