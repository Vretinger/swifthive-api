from rest_framework import generics, permissions
from rest_framework import serializers
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.response import Response
from rest_framework import status

# ✅ Create Job Listing (Only Clients)
class CreateListingAPI(generics.CreateAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts can create listings."})
        serializer.save(Company=user.company)

# ✅ List Job Listings (Anyone Can See)
class ListListingsAPI(generics.ListAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]

# ✅ Edit & Delete Listings (Only Listing Owner)
class EditDeleteListingAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Listing.objects.filter(Company=user.company, id=self.kwargs["pk"])

