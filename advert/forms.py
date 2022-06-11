from django import forms
from loppises.widgets import CustomClearableFileInput
from loppises.models import Loppis, County


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class LoppisForm(forms.ModelForm):

    class Meta:
        model = Loppis
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'start_time': TimeInput(),
            'end_time': TimeInput(),
        }
        
        fields = (
            'title', 'start_date', 'end_date',
            'start_time', 'end_time', 'country',
            'postcode', 'county', 'city',
            'street_address', 'phone_number',
            'image', 'description',
            )

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        counties = County.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in counties]

        self.fields['county'].choices = friendly_names
        self.fields['country'].widget.attrs['value'] = 'Sweden'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
