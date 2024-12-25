from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer
from django.http import HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated
from job_listings.models import JobListing, JobApplication
from job_listings.serializers import JobListingSerializer


class ClientList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class ClientDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)


class ClientDashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Ensure that the user is a client
        try:
            client = Client.objects.get(user=request.user)
        except Client.DoesNotExist:
            return HttpResponseForbidden("Only clients can view this dashboard.")

        # Get all job listings created by the client
        job_listings = JobListing.objects.filter(client=client)
        job_listings_data = []

        for job_listing in job_listings:
            # Get job applications for each listing
            applications = JobApplication.objects.filter(job_listing=job_listing)
            job_listings_data.append({
                'job_listing': JobListingSerializer(job_listing).data,
                'applications': [
                    {
                        'freelancer': app.freelancer.username,
                        'status': app.status
                    } for app in applications
                ]
            })

        return Response({'job_listings': job_listings_data})
