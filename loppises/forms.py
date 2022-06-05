from django import forms
from .models import Loppis, County


class LoppisForm(forms.ModelForm):

    class Meta:
        model = Loppis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        counties = County.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in counties]

        self.fields['county'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
