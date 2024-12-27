from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    company = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def validate(self, data):
        if data.get('role') == 'client' and not data.get('company'):
            raise serializers.ValidationError({'company': "This field is required for clients."})
        return data

    def custom_signup(self, request, user):
        user.role = self.validated_data.get('role', 'freelancer')
        user.company = self.validated_data.get('company', '')
        user.save()
