from rest_framework import generics, permissions
from rest_framework import serializers
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework.response import Response
from rest_framework import status

# Apply for a Job
class ApplyForJobAPI(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        listing = serializer.validated_data['listing']

        # Optionally, ensure the listing is active and still open
        if not listing.is_active:
            raise serializers.ValidationError({"error": "This job listing is no longer active."})
        
        serializer.save(applicant=user)

class ListUserApplicationsAPI(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user)

class ListJobApplicationsAPI(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts can view applications."})
        
        listing_id = self.kwargs.get("listing_id")
        return JobApplication.objects.filter(listing__Company=user.company, listing_id=listing_id)


class UpdateApplicationStatusAPI(generics.UpdateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts can update applications."})
        
        return JobApplication.objects.filter(listing__Company=user.company)

    def perform_update(self, serializer):
        serializer.save()
