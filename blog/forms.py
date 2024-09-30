from .models import Rating
from django import forms


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['percentage_score']  # Ensure you're editing this field
        widgets = {
            'percentage_score': forms.NumberInput(attrs={
                'class': 'form-control',  # Use a number input in HTML
                'min': '0',
                'max': '100',
            }),
        }