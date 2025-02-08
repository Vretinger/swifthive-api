from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, FreelancerProfile, ClientProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    print(f"Signal triggered for user: {instance.email}, created: {created}, role: {instance.role}")
    
    if created:  # Only create a profile if the user is newly created
        if instance.role == 'freelancer' and not FreelancerProfile.objects.filter(user=instance).exists():
            FreelancerProfile.objects.create(user=instance)
            print(f"FreelancerProfile created for {instance.email}")
        elif instance.role == 'client' and not ClientProfile.objects.filter(user=instance).exists():
            ClientProfile.objects.create(user=instance)
            print(f"ClientProfile created for {instance.email}")
