from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Company, FreelancerProfile, Skill
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

class FreelancerProfileForm(forms.ModelForm):
    class Meta:
        model = FreelancerProfile
        fields = ['bio', 'skills', 'custom_skills', 'experience', 'portfolio_link', 'hourly_rate', 'location', 'availability_status', 'profile_picture']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,  # Predefined skills as checkboxes
        }

    def clean_custom_skills(self):
        custom_skills = self.cleaned_data.get('custom_skills', '').strip()
        if custom_skills and len(custom_skills.split(',')) > 5:
            raise forms.ValidationError("Please limit custom skills to 5.")
        return custom_skills