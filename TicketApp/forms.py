from django import forms
from TicketApp.models import Ticket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'number_of_person', 'person_mail_address', 'person_mobile_number'
        ]
        widgets = {
            'number_of_person' : forms.NumberInput(attrs={'class': 'person-count-field-ticket', 'id': 'ticket-field-id', 'placeholder': 'Number of Tickets'}),
            'person_mail_address' : forms.TextInput(attrs={'class': 'person-mail-field-ticket', 'id': 'ticket-field-id', 'placeholder': 'Enter Your Email'}), 
            'person_mobile_number' : forms.TextInput(attrs={'class': 'person-number-field-ticket', 'id': 'ticket-field-id', 'type': 'tel', 'placeholder': 'Enter Your Phone Number'}),
        }
class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'number_of_person', 'person_mail_address', 'person_mobile_number'
        ]