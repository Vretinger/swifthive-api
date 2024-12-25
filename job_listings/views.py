from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import JobListing
from .serializers import JobListingSerializer

class JobListingList(APIView):
    def get(self, request):
        job_listings = JobListing.objects.filter(is_active=True)
        serializer = JobListingSerializer(job_listings, many=True)
        return Response(serializer.data)


class JobListingCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        client = Client.objects.get(user=request.user)
        data = request.data
        data['client'] = client.id
        serializer = JobListingSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
