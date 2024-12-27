from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='freelancer')
    company = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.role == 'client' and not self.company:
            raise ValueError("Company is required for clients.")
        super().save(*args, **kwargs)
