from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from django.http import HttpResponseForbidden
from .models import JobListing, JobApplication, ClientProfile
from .serializers import JobListingSerializer
from django_filters import rest_framework as filters


# Define the filter for Job Listings
class JobListingFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    company_name = filters.CharFilter(lookup_expr='icontains')
    job_type = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = JobListing
        fields = ['title', 'company_name', 'job_type']

class JobListingList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        job_listings = JobListing.objects.all()  # You can customize this if needed

        # Apply the filter
        filter_backends = [DjangoFilterBackend]
        job_listings = JobListingFilter(request.GET, queryset=job_listings).qs

        serializer = JobListingSerializer(job_listings, many=True)
        return Response(serializer.data)

class JobListingCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if the user is a client
        try:
            client = ClientProfile.objects.get(user=request.user)
        except ClientProfile.DoesNotExist:
            return HttpResponseForbidden("Only clients can create job listings.")
        
        data = request.data
        data['client'] = client.id
        serializer = JobListingSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class JobApplicationCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, job_id):
        # Check if the user is a freelancer
        if not hasattr(request.user, 'freelancer'):  # Assuming you have a freelancer model associated with the user
            return HttpResponseForbidden("Only freelancers can apply for job listings.")
        
        # Get the job listing
        job_listing = get_object_or_404(JobListing, id=job_id)

        # Create a job application
        job_application = JobApplication.objects.create(
            freelancer=request.user,
            job_listing=job_listing
        )

        return Response({
            'message': 'Application submitted successfully',
            'application_id': job_application.id
        }, status=201)