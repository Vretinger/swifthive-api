from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    username = None  # Disable the 'username' field
    email = serializers.EmailField(required=True)
    role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    company = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def validate(self, data):
        role = data.get('role')
        if role == 'client' and not data.get('company'):
            raise serializers.ValidationError({'company': "This field is required for clients."})
        elif role not in dict(CustomUser.ROLE_CHOICES).keys():
            raise serializers.ValidationError({'role': "Invalid role specified."})
        return data

    def save(self, request):
        # Collect the user data from the validated data and save the user
        user = CustomUser.objects.create(
            email=self.validated_data['email'],
            role=self.validated_data['role'],
            company=self.validated_data.get('company', ''),
        )
        user.set_password(self.validated_data['password1'])  # Set password
        user.save()
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'role', 'company', 'password']
        extra_kwargs = {
            'password': {'write_only': True}, 
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user