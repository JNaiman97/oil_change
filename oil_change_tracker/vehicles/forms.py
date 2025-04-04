from django import forms
from .models import Vehicle
from .models import OilChangeRecord

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner']

class OilChangeForm(forms.ModelForm):
    class Meta:
        model = OilChangeRecord
        fields = ['date', 'kilometrage', 'next_reminder']