from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Company
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
    CATEGORY_CHOICES = [
        ("tech", "Tech"),
        ("finance", "Finance"),
        ("healthcare", "Healthcare"),
        ("marketing", "Marketing"),
        ("education", "Education"),
        ("other", "Other"),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=300, help_text="A short summary of the job")
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. $50,000 - $70,000")
    employment_type = models.CharField(
        max_length=50,
        choices=[("full-time", "Full Time"), ("part-time", "Part Time"), ("contract", "Contract")],
        default="full-time",
    )

    REMOTE_CHOICES = [
        ('onsite', 'Onsite'),
        ('hybrid', 'Hybrid'),
        ('remote', 'Remote'),
    ]
    
    remote = models.CharField(max_length=7, choices=REMOTE_CHOICES, default='onsite')
    is_active = models.BooleanField(default=True)
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_jobs")


    def __str__(self):
        return f"{self.title} at {self.company.name if self.company else 'Unknown Company'}"
