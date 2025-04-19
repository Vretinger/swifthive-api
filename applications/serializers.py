from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    listing_title = serializers.CharField(source="listing.title", read_only=True)
    company_name = serializers.CharField(source="listing.company.name", read_only=True)

    
    freelancer_id = serializers.IntegerField(source="applicant.id", read_only=True)

    class Meta:
        model = JobApplication
        fields = '__all__'
