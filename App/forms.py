from django import forms
from .models import Booking
# from django.forms import ModelForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        # fields = [
        #     'person_name',
        #     'person_mail',
        #     'person_address',
        #     'person_number',
        #     'event_title',
        #     'person_count',
        # ]

        widgets = {
            'person_name' : forms.TextInput(attrs={'class': 'person-name-field', 'id': 'field-id', 'placeholder': 'Enter Your Name'}),
            'person_mail' : forms.TextInput(attrs={'class': 'person-mail-field', 'id': 'field-id', 'placeholder': 'Enter Your Email'}), 
            'person_address' : forms.Textarea(attrs={'class': 'person-address-field', 'id': 'field-id-address', 'placeholder': 'Enter Your Address'}),
            'person_number' : forms.TextInput(attrs={'class': 'person-number-field', 'id': 'field-id', 'type': 'tel', 'placeholder': 'Enter Your Phone Number'}),
            'event_title' : forms.Select(attrs={'class': 'event-title-field', 'id': 'field-id', 'placeholder': 'Select Event'}),
            'person_count' : forms.NumberInput(attrs={'class': 'person-count-field', 'id': 'field-id', 'placeholder': 'Number of Person'}),
        }