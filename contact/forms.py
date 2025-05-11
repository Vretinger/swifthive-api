# forms.py
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    freelancer_email = forms.EmailField() 
