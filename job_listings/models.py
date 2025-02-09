from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Company



class Listing(models.Model):
    CATEGORY_CHOICES = [
        ("tech", "Tech"),
        ("finance", "Finance"),
        ("healthcare", "Healthcare"),
        ("marketing", "Marketing"),
        ("education", "Education"),
        ("other", "Other"),
    ]

    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
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
    remote = models.BooleanField(default=False)
    application_deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.Company.name if self.Company else 'Unknown Company'}"