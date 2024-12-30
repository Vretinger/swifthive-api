from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30, required=True)
    surname = serializers.CharField(max_length=30, required=True)
    role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    company = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def validate(self, data):
        if data.get('role') == 'client' and not data.get('company'):
            raise serializers.ValidationError({'company': "This field is required for clients."})
        return data

    def custom_signup(self, request, user):
        # Set the first name, surname, role, and company fields on the user object
        user.first_name = self.validated_data.get('first_name')
        user.surname = self.validated_data.get('surname')
        user.role = self.validated_data.get('role', 'freelancer')
        user.company = self.validated_data.get('company', '')
        user.save()

        return user
