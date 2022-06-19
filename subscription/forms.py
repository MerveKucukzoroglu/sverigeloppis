"""Forms file for newsletter subscription"""
from django import forms
from .models import Subscriptions


class NewsletterForm(forms.ModelForm):
    """newsletter form"""
    email = forms.EmailField(label='')

    class Meta:
        """newsletter meta class"""
        model = Subscriptions
        fields = ('email',)

    def clean_email(self):
        """check if email given already exists in database"""
        email = self.cleaned_data.get("email")
        subscriber = Subscriptions.objects.filter(email__iexact=email)
        if subscriber.exists():
            raise forms.ValidationError("This email already exists")
        return email
