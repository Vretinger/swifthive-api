from django.urls import path
from .views import FreelancerListView, FreelancerDetailView, ClientListView, ClientDetailView, JobbListingView, CreateListingAPI


urlpatterns = [
    path('freelancers/', FreelancerListView.as_view(), name='freelancer-list'),
    path('freelancers/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('listing/', JobbListingView.as_view(), name='listing-detail'),
    path("create_listing/", CreateListingAPI.as_view(), name="create_listing"),
]
