"""Forms file for newsletter subscription"""
from .models import Subscriptions
from django import forms


class NewsletterForm(forms.ModelForm):
    """question form"""
    email = forms.EmailField(label='')

    class Meta:
        model = Subscriptions
        fields = ('email',)

    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        subscriber = Subscriptions.objects.filter(email__iexact=email)
        if subscriber.exists():
            raise forms.ValidationError("This email already exists")
        return email
