from .models import Rating, Stamp
from django import forms


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['percentage_score']
        widgets = {
            'percentage_score': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '100',
            }),
        }


class StampForm(forms.ModelForm):
    class Meta:
        model = Stamp
        fields = ['title', 'country', 'location', 'image', 'status']
