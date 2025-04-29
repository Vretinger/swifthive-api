from rest_framework import serializers
from .models import JobApplication
from job_listings.models import Listing  # import the Listing model

class JobApplicationSerializer(serializers.ModelSerializer):
    # Fields from the Job Listing model
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    category = serializers.CharField(source='listing.category', read_only=True)
    location = serializers.CharField(source='listing.location', read_only=True)
    short_description = serializers.CharField(source='listing.short_description', read_only=True)
    company_name = serializers.CharField(source='listing.company.name', read_only=True)  # Access company name

    # Fields from the Job Application model
    freelancer_id = serializers.IntegerField(source='applicant.id', read_only=True)

    # Adding status to be writable
    status = serializers.ChoiceField(choices=JobApplication.STATUS_CHOICES, required=False)  # Assuming STATUS_CHOICES are defined in JobApplication

    class Meta:
        model = JobApplication
        fields = [
            'id', 'listing', 'listing_title', 'category', 'location', 'short_description',
            'company_name', 'status', 'applied_at', 'resume', 'cover_letter', 'freelancer_id', 'applicant',
        ]
        read_only_fields = ['listing', 'applied_at', 'resume', 'cover_letter', 'freelancer_id']