from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Company
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
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'role', 'company')