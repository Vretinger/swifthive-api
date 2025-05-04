from rest_framework import serializers
from .models import JobApplication
from job_listings.models import Listing
from cloudinary.uploader import upload

class JobApplicationSerializer(serializers.ModelSerializer):
    # Fields from the Job Listing model
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    category = serializers.CharField(source='listing.category', read_only=True)
    location = serializers.CharField(source='listing.location', read_only=True)
    short_description = serializers.CharField(source='listing.short_description', read_only=True)
    company_name = serializers.CharField(source='listing.company.name', read_only=True) 
    resume = serializers.FileField(write_only=True)
    resume_url = serializers.URLField(read_only=True, source='resume')

    # Fields from the Job Application model
    freelancer_id = serializers.IntegerField(source='applicant.id', read_only=True)

    # Adding status to be writable
    status = serializers.ChoiceField(choices=JobApplication.STATUS_CHOICES, required=False)  # Assuming STATUS_CHOICES are defined in JobApplication

    class Meta:
        model = JobApplication
        fields = [
            'id', 'listing', 'listing_title', 'category', 'location', 'short_description',
            'company_name', 'status', 'applied_at', 'resume', 'resume_url', 'cover_letter', 'freelancer_id', 'applicant',
        ]
        read_only_fields = ['listing', 'applied_at', 'resume', 'cover_letter', 'freelancer_id']

    def create(self, validated_data):
        resume_file = validated_data.pop('resume')

        # Upload to Cloudinary
        result = upload(resume_file, resource_type="auto", folder="resumes")
        resume_url = result.get("secure_url")

        # Add the URL back into the validated_data
        validated_data['resume'] = resume_url

        return JobApplication.objects.create(**validated_data)