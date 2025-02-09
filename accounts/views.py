from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from dj_rest_auth.registration.views import RegisterView
from .models import FreelancerProfile, ClientProfile
from .serializers import FreelancerProfileSerializer, ClientProfileSerializer, CustomRegisterSerializer, ListingSerializer
from .models import Listing
from rest_framework.response import Response



class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    permission_classes = [permissions.AllowAny]

class FreelancerListView(generics.ListAPIView):
    queryset = FreelancerProfile.objects.all()
    serializer_class = FreelancerProfileSerializer
    permission_classes = [permissions.AllowAny]

class FreelancerDetailView(generics.RetrieveUpdateAPIView):
    queryset = FreelancerProfile.objects.all()
    serializer_class = FreelancerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientListView(generics.ListAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.AllowAny]

class ClientDetailView(generics.RetrieveUpdateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  

class CreateListingAPI(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    def post(self, request):
        user = request.user

        # Ensure only clients (not admin/staff) can create listings
        if not hasattr(user, "company"):  # If user has no associated company, deny access
            return Response(
                {"error": "Only client accounts can create listings."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            listing = serializer.save(Company=user.company)  # Assign company automatically
            return Response(
                {"message": "Listing created successfully!", "listing_id": listing.id},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListListingsAPI(APIView):
    permission_classes = [AllowAny]  # Open to everyone

    def get(self, request):
        listings = Listing.objects.all()  # Get all listings
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)