from django.contrib.auth.backends import BaseBackend
from accounts.models import CustomUser 
from freelancers.models import Freelancer
from clients.models import Client

class EmailAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to authenticate with email for both Freelancers and Clients
        try:
            # Check if the user exists by email in the CustomUser model
            user = CustomUser.objects.get(email=username)
            
            # If the user exists, check the password
            if user.check_password(password):
                # Return the user if they exist as a Freelancer or Client
                if hasattr(user, 'freelancer'):
                    return user
                if hasattr(user, 'client'):
                    return user
        except CustomUser.DoesNotExist:
            return None
        
        return None  # Authentication failed

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
