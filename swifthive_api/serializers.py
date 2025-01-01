from dj_rest_auth.serializers import UserDetailsSerializer
from .models import CustomUser


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'first_name', 'last_name', 'role']