from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    ]
    
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(max_length=30, verbose_name="last_name")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='freelancer')
    company = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'  # Use email for login
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']  # Add role to required fields
    
    def save(self, *args, **kwargs):
        if self.role == 'client' and not self.company:
            raise ValueError("Company is required for clients.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
