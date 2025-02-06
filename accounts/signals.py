from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Freelancer, Client

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'freelancer':
            Freelancer.objects.create(user=instance)
        elif instance.role == 'client':
            Client.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """ Ensures the profile is saved whenever the user is updated. """
    if instance.role == 'freelancer' and hasattr(instance, 'freelancer_profile'):
        instance.freelancer_profile.save()
    elif instance.role == 'client' and hasattr(instance, 'client_profile'):
        instance.client_profile.save()
