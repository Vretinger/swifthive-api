from django.db import models
from django.conf import settings  # Use settings.AUTH_USER_MODEL

class Freelancer(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
        ('On Leave', 'On Leave'),
    ]

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='freelancer_profile'
    )
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField('Skill', blank=True)
    experience = models.TextField(blank=True, null=True)
    portfolio_link = models.URLField(blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    availability_status = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default='Available'
    )
    profile_picture = models.ImageField(
        upload_to='freelancer_pics/', 
        default='default_profile.png'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner.email}'s Profile"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
