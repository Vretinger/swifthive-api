# clients/models.py
from django.db import models
from django.contrib.auth.models import User


# Company Model
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# Client Model
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='clients', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='client_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"


# Listing Model (for creating and managing listings)
class Listing(models.Model):
    client = models.ForeignKey(Client, related_name='listings', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='listings', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
