from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import JobApplication, JobListing

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['id', 'client', 'title', 'description', 'is_active', 'created_at', 'location']


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'freelancer', 'job_listing', 'application_date']
