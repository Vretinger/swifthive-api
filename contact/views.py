from rest_framework import generics, status
from rest_framework.permissions import AllowAny  # Allow any user, authenticated or not
from .serializers import ContactSerializer
from applications.send_email import send_email_via_brevo
from rest_framework.response import Response


class ContactFreelancerAPI(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]  # Allow any user to submit the form, no authentication required

    def perform_create(self, serializer):
        # Get data from the request
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        freelancer_email = serializer.validated_data['freelancer_email']

        # Send email via Brevo (or your chosen email service)
        try:
            send_email_via_brevo(subject, message, freelancer_email)
        except Exception as e:
            # Handle error if email sending fails
            return Response({"error": "Failed to send email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Return a success message after email is sent
        return Response({"message": "Message sent successfully!"}, status=status.HTTP_200_OK)
