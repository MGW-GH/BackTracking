from django import forms
from .models import Stamp
from django_countries import countries


class CountrySearchForm(forms.Form):
    country = forms.ChoiceField(
        choices=[(code, name) for code, name in countries]
    )
