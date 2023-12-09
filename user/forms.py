from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

        # widgets = {
        #     'username' : forms.TextInput(attrs={}),
        #     'email' : forms.EmailInput(attrs={}),
        #     'password1' : forms.PasswordInput(attrs={'placeholder':'Create a password'}),
        #     'password2' : forms.PasswordInput(attrs={'placeholder':'Confirm password'}),
        # }