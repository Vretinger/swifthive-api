from django.urls import path
from .views import ContactFreelancerAPI

urlpatterns = [
    path('contact-freelancer/', ContactFreelancerAPI.as_view(), name='contact_freelancer'),
]
