from rest_framework import generics, permissions, serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import JobApplication
from .serializers import JobApplicationSerializer
from accounts.models import FreelancerProfile, ClientProfile
from job_listings.models import Listing
from django.core.mail import send_mail

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def decline_application(request, job_id, freelancer_id):
    reason = request.data.get("reason", "").strip()
    if len(reason) > 300:
        return Response({"error": "Reason too long."}, status=400)

    freelancer = get_object_or_404(FreelancerProfile, user_id=freelancer_id)
    application = get_object_or_404(JobApplication, listing_id=job_id, applicant_id=freelancer_id)

    # Get client profile and company name
    client_profile = get_object_or_404(ClientProfile, user_id=application.client.id)
    company_name = client_profile.company_name if client_profile.company_name else "The SwiftHive Team"

    # Email decline message
    subject = "Your Application Update"
    message = (
        f"Hi {freelancer.user.first_name},\n\n"
        "Thank you for your application. After reviewing all submissions, we've decided to move forward with other candidates.\n\n"
        f"Reason: {reason if reason else 'No specific reason provided.'}\n\n"
        "We truly appreciate your interest and wish you the best in your job search.\n\n"
        f"Best regards,\n{company_name}\n"
    )

    try:
        send_mail(
            subject,
            message,
            "no-reply@swifthive.com",
            [freelancer.user.email],
            fail_silently=False,
        )
    except Exception as e:
        return Response({"error": "Failed to send email.", "details": str(e)}, status=500)

    # Update application status
    application.status = "rejected"
    application.save()

    return Response({"message": "Decline email sent."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_application(request, job_id, freelancer_id):
    interview_message = request.data.get("interview_message", "").strip()
    if len(interview_message) > 500:
        return Response({"error": "Interview message too long."}, status=400)

    freelancer = get_object_or_404(FreelancerProfile, user_id=freelancer_id)
    application = get_object_or_404(JobApplication, listing_id=job_id, applicant_id=freelancer_id)

    # Get client profile and company name
    client_profile = get_object_or_404(ClientProfile, user_id=application.client.id)
    company_name = client_profile.company_name if client_profile.company_name else "The SwiftHive Team"

    # Email approve message
    subject = "Your Application Status - Interview Invitation"
    message = (
        f"Hi {freelancer.user.first_name},\n\n"
        "We are excited to inform you that your application has been approved for the next step in the hiring process.\n\n"
        "We would like to schedule an interview with you. Our team will reach out soon to arrange a time that works for you.\n\n"
        f"Additional Message: {interview_message if interview_message else 'We look forward to speaking with you.'}\n\n"
        "Best regards,\n"
        f"{company_name}\n"
    )

    try:
        send_mail(
            subject,
            message,
            "no-reply@swifthive.com",
            [freelancer.user.email],
            fail_silently=False,
        )
    except Exception as e:
        return Response({"error": "Failed to send email.", "details": str(e)}, status=500)

    # Update application status to 'approved' for interview
    application.status = "accepted"
    application.save()

    return Response({"message": "Interview invitation email sent."}, status=status.HTTP_200_OK)

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