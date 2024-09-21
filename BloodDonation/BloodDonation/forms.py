# blood_donation/forms.py
from django import forms
from .models import BloodDonationRequest

class BloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonationRequest
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality']
