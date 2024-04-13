from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model= Donor
        fields=['name','blood_group','email','phone_number']
