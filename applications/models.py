from django.db import models
from django.conf import settings  # Import settings for AUTH_USER_MODEL
from job_listings.models import Listing

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'applicant')  # Prevent duplicate applications

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title} ({self.status})"
