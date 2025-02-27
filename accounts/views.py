from rest_framework import generics, permissions
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from .models import FreelancerProfile, ClientProfile, Skill
from .serializers import FreelancerProfileSerializer, ClientProfileSerializer, CustomRegisterSerializer, SkillSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    permission_classes = [permissions.AllowAny]

class FreelancerListView(generics.ListAPIView):
    queryset = FreelancerProfile.objects.all()
    serializer_class = FreelancerProfileSerializer
    permission_classes = [permissions.AllowAny]

class FreelancerDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = FreelancerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "user_id"  # Tell Django to use 'user_id' instead of 'pk'

    def get_queryset(self):
        return FreelancerProfile.objects.all()

class ClientListView(generics.ListAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.AllowAny]

class ClientDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  
    lookup_field = "user_id"  # Tell Django to use 'user_id' instead of 'pk'

    def get_queryset(self):
        return ClientProfile.objects.all()

class SkillListView(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_name = self.request.query_params.get('category', None)
        
        if category_name:
            # Filter by category name if provided in the query param
            return Skill.objects.filter(category__name=category_name)
        else:
            # Return all skills if no category filter is applied
            return Skill.objects.all()