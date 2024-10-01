from django import forms
from .models import Stamp

class CountrySearchForm(forms.Form):
    country = forms.ChoiceField(choices=[], label="Select Country")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate the choices with unique country values from the Stamp model
        self.fields['country'].choices = [(stamp.country, stamp.country) for stamp in Stamp.objects.all().distinct()]