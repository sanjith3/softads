# enquiries/forms.py
from django import forms #type: ignore
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'contact_number', 'ad_title']