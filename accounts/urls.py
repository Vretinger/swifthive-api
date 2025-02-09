from django.urls import path, include
from .views import CustomRegisterView, FreelancerListView, FreelancerDetailView, ClientListView, ClientDetailView, JobbListingView, create_listing
from dj_rest_auth import views as dj_rest_auth_views

urlpatterns = [
    path('freelancers/', FreelancerListView.as_view(), name='freelancer-list'),
    path('freelancers/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('listing/', JobbListingView.as_view(), name='listing-detail'),
    path('create_listing/', create_listing.as_view(), name='create_listing'),
]
