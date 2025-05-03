from django.urls import path
from .views import ListListingsAPI, ViewListingAPI, CreateListingAPI, EditDeleteListingAPI, MyListingsAPI, MyListingDetailAPI

urlpatterns = [
    path('listings/', ListListingsAPI.as_view(), name='list-listings'),
    path('listings/<int:pk>/', ViewListingAPI.as_view(), name='view-listing'),  # View job listing
    path('my-listings/', MyListingsAPI.as_view(), name="my-job-listings"),
    path('my-detail/<int:pk>/', MyListingDetailAPI.as_view(), name="my-job-listing-detail"),
    path('listings/<int:pk>/edit/', EditDeleteListingAPI.as_view(), name='edit-listing'),
    path('listings/<int:pk>/delete/', EditDeleteListingAPI.as_view(), name='delete-listing'),
    path('create/', CreateListingAPI.as_view(), name='create-listing'),
]
