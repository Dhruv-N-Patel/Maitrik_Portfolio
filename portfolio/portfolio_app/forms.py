from django import forms
from .models import ContactForm

COUNTRY_CODES = (
    ('+91', '+91 - India'),
    # Add more country codes as needed
)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email','phone_country_code', 'phone_number', 'message']

    phone_country_code = forms.ChoiceField(choices=COUNTRY_CODES, initial='+91', label='Country Code')
