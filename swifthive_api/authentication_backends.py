from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from freelancers.models import Freelancer
from clients.models import Client

class EmailAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to authenticate with email for both Freelancers and Clients

        try:
            # First, check if the user is a Freelancer
            user = User.objects.get(email=username)
            
            # If user exists, authenticate with the password
            if user.check_password(password):
                # You can check if the user is a Freelancer or Client, or just return the User object
                if hasattr(user, 'freelancer'):
                    return user
                if hasattr(user, 'client'):
                    return user

        except User.DoesNotExist:
            return None
        
        return None  # Authentication failed

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
