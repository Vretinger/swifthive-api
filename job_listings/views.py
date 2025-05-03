from rest_framework import generics, permissions, serializers
from rest_framework.exceptions import NotFound
from .models import Listing
from .serializers import ListingSerializer


# ✅ Public Job Listings (Anyone Can See)
class ListListingsAPI(generics.ListAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]

# ✅ Public Job Detail (Anyone Can View)
class ViewListingAPI(generics.RetrieveAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]


# ✅ Create Job Listing (Only Clients)
class CreateListingAPI(generics.CreateAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts can create listings."})
        serializer.save(company=user.company)

# ✅ List Job Listings Created by the Logged-In Client
class MyListingsAPI(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts have listings."})
        
        # Return all listings by the logged-in client's company
        return Listing.objects.filter(company=user.company)
    

# ✅ View Job Details Created by the Logged-In Client (Only Client)
class MyListingDetailAPI(generics.RetrieveAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not hasattr(user, "company"):
            raise serializers.ValidationError({"error": "Only client accounts have listings."})
        return Listing.objects.filter(company=user.company)



# ✅ Edit & Delete Listings (Only Listing Owner)
class EditDeleteListingAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        listing_id = self.kwargs.get("pk")

        try:
            listing = Listing.objects.get(id=listing_id, company=user.company)
        except Listing.DoesNotExist:
            raise NotFound("Job listing not found or you do not have permission to edit it.")

        return listing
