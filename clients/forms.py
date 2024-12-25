from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'job_title', 'phone_number', 'email', 'profile_picture']