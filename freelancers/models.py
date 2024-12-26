from django.contrib.auth.models import User
from django.db import models

class Freelancer(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
        ('On Leave', 'On Leave'),
    ]

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # Freelancer's short bio
    skills = models.ManyToManyField('Skill', blank=True)  # Reference to skills model
    experience = models.TextField(blank=True, null=True)  # Freelance experience
    portfolio_link = models.URLField(blank=True, null=True)  # Link to portfolio
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Freelancer's hourly rate
    location = models.CharField(max_length=255, blank=True, null=True)  # Freelancer's location
    availability_status = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='Available'
    )
    profile_picture = models.ImageField(upload_to='freelancer_pics/', default='../default_profile_rnezic')  # Profile picture
    created_at = models.DateTimeField(auto_now_add=True)  # Profile creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Profile update timestamp

    def __str__(self):
        return f"{self.owner.username}'s Profile"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name of the skill
    description = models.TextField(blank=True, null=True)  # Description of the skill (optional)

    def __str__(self):
        return self.name
