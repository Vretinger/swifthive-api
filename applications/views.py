from rest_framework import generics, permissions, serializers, status
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework.response import Response
from accounts.models import FreelancerProfile
from job_listings.models import Listing

class ApplyForJobAPI(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        listing_id = request.data.get("listing")
        cover_letter = request.data.get("cover_letter", "")
        uploaded_resume = request.FILES.get("resume", None)
        use_profile_resume = request.data.get("use_profile_resume", "false").lower() == "true"

        # Check for valid listing
        try:
            listing = Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            return Response({"error": "Listing not found."}, status=status.HTTP_404_NOT_FOUND)

        if not listing.is_active:
            return Response({"error": "This job listing is no longer active."}, status=status.HTTP_400_BAD_REQUEST)

        # Check for duplicate application
        if JobApplication.objects.filter(applicant=user, listing=listing).exists():
            return Response({"error": "You have already applied for this job."}, status=status.HTTP_400_BAD_REQUEST)

        # Determine which resume to use
        resume = None
        if use_profile_resume and not uploaded_resume:
            try:
                resume = user.FreelancerProfile.resume
                if not resume:
                    raise Exception("No resume found in profile.")
            except Exception:
                return Response({"error": "Profile resume not found."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            resume = uploaded_resume

        if not resume:
            return Response({"error": "Resume is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create application
        application = JobApplication.objects.create(
            listing=listing,
            applicant=user,
            cover_letter=cover_letter,
            resume=resume,
        )

        return Response({"message": "Application submitted successfully."}, status=status.HTTP_201_CREATED)

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
        return JobApplication.objects.filter(listing__company=user.company, listing_id=listing_id)


class UpdateApplicationStatusAPI(generics.UpdateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts can update applications."})
        
        return JobApplication.objects.filter(listing__company=user.company)

    def perform_update(self, serializer):
        serializer.save()
