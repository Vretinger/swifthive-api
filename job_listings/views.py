from rest_framework import generics, permissions, serializers, status
from rest_framework.exceptions import NotFound
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.response import Response


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

# ✅ View Job Listing (Anyone Can View)
class ViewListingAPI(generics.RetrieveAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view

# ✅ Edit & Delete Listings (Only Listing Owner)
class EditDeleteListingAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs.get("pk", "")

        # Ensure that pk is a valid integer
        if not pk or not pk.isdigit():
            raise NotFound("Job listing not found.")

        queryset = Listing.objects.filter(Company=user.company, id=int(pk))
        if not queryset.exists():
            raise NotFound("Job listing not found.")
        
        return queryset
