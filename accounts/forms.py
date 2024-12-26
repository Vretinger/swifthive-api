from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from client.models import Company  # Import the Company model from the client app

class CustomUserSignupForm(UserCreationForm):
    ROLE_CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        required=False,
        help_text="Required if signing up as a client."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'company']
