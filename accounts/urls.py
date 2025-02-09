from django.urls import path
from .views import FreelancerListView, FreelancerDetailView, ClientListView, ClientDetailView, ListListingsAPI, CreateListingAPI


urlpatterns = [
    path('freelancers/', FreelancerListView.as_view(), name='freelancer-list'),
    path('freelancers/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path("listings/", ListListingsAPI.as_view(), name="listings"),
    path("create_listing/", CreateListingAPI.as_view(), name="create_listing"),
]
