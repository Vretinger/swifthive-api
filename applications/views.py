from rest_framework import generics, permissions, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from applications.send_email import send_email_via_brevo
from .models import JobApplication
from .serializers import JobApplicationSerializer
from accounts.models import FreelancerProfile, ClientProfile
from job_listings.models import Listing

class UpdateApplicationStatusAPI(generics.UpdateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Only allow clients to view and update applications
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts can update applications."})

        # Retrieve applications associated with the user's company
        return JobApplication.objects.filter(listing__company=user.company)

    def perform_update(self, serializer):
        application = serializer.save()  # Save the updated application status
        status = application.status
        
        # Send email notification based on the new status
        if status == "accepted":
            self.send_approval_email(application)
        elif status == "rejected":
            self.send_decline_email(application)
        else:
            raise serializers.ValidationError({"error": "Invalid status for email notification."})

    def send_approval_email(self, application):
        freelancer = application.applicant
        client_user = application.listing.created_by
        client_profile = get_object_or_404(ClientProfile, user=client_user)
        company_name = client_profile.company_name or "The SwiftHive Team"

        subject = "Your Application Status - Interview Invitation"
        html_content = (
            f"<p>Hi {freelancer.first_name},</p>"
            "<p>We are excited to inform you that your application has been approved for the next step in the hiring process.</p>"
            "<p>We would like to schedule an interview with you. Our team will reach out soon to arrange a time that works for you.</p>"
            f"<p>Best regards,<br>{company_name}</p>"
        )

        try:
            send_email_via_brevo(subject, html_content, freelancer.email)
        except ValidationError as e:
            raise serializers.ValidationError({
                "error": "Failed to send approval email.",
                "details": str(e)
            })

    def send_decline_email(self, application):
        freelancer = application.applicant
        client_user = application.listing.created_by
        client_profile = get_object_or_404(ClientProfile, user=client_user)
        company_name = client_profile.company_name or "The SwiftHive Team"
        reason = getattr(application, "status_change_reason", "No specific reason provided.")

        subject = "Your Application Update"
        html_content = (
            f"<p>Hi {freelancer.first_name},</p>"
            "<p>Thank you for your application. After reviewing all submissions, we've decided to move forward with other candidates.</p>"
            f"<p><strong>Reason:</strong> {reason}</p>"
            "<p>We truly appreciate your interest and wish you the best in your job search.</p>"
            f"<p>Best regards,<br>{company_name}</p>"
        )

        try:
            send_email_via_brevo(subject, html_content, freelancer.email)
        except ValidationError as e:
            raise serializers.ValidationError({
                "error": "Failed to send decline email.",
                "details": str(e)
            })

class ApplyForJobAPI(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        listing_id = request.data.get("listing")

        # Validate listing
        try:
            listing = Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            return Response({"error": "Listing not found."}, status=status.HTTP_404_NOT_FOUND)

        if not listing.is_active:
            return Response({"error": "This job listing is no longer active."}, status=status.HTTP_400_BAD_REQUEST)

        # Check duplicate
        if JobApplication.objects.filter(applicant=user, listing=listing).exists():
            return Response({"error": "You have already applied for this job."}, status=status.HTTP_400_BAD_REQUEST)

        # Use resume from profile if needed
        if request.data.get("use_profile_resume", "false").lower() == "true":
            try:
                resume_url = user.freelancerprofile.resume
                if not resume_url:
                    raise Exception()
                request.data._mutable = True  # Only if QueryDict is immutable
                request.data["resume"] = resume_url  # serializer will treat this as URL
            except:
                return Response({"error": "Resume not found in profile."}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


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
    
class HasAppliedAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, listing_id):
        user = request.user

        # Remove freelancer-specific restriction
        has_applied = JobApplication.objects.filter(applicant=user, listing_id=listing_id).exists()
        return Response({"has_applied": has_applied})
