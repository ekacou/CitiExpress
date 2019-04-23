from django import forms
from .models import Client


class ClientSignUp(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["username", "first_name", "last_name", "contact", "email", "password"]
        widget = {

            "password": forms.PasswordInput(),
        }


class ClientSignIn(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'password']
        widget = {

            "password": forms.PasswordInput(),
        }
