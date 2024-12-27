from django.db import models
from django.conf import settings  # Use settings.AUTH_USER_MODEL

# Company Model
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# Client Model
class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use custom user model
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='clients', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='client_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.company.name}"  # Use email for clarity


# Listing Model
class Listing(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title
