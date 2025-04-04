from django import forms
from .models import Vehicle
from .models import OilChangeRecord

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner']

class OilChangeForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': 'DD-MM-YYYY',
                'class': 'form-control'
            }
        ),
        input_formats=['%d-%m-%Y']
    )
    next_reminder = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': 'DD-MM-YYYY',
                'class': 'form-control'
            }
        ),
        input_formats=['%d-%m-%Y']
    )

    class Meta:
        model = OilChangeRecord
        fields = ['date', 'kilometrage', 'next_reminder']