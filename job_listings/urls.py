from django.urls import path
from .views import JobListingList, JobListingCreate

urlpatterns = [
    path('api/listings/', JobListingList.as_view(), name='job_listing_list_api'),
    path('api/listings/create/', JobListingCreate.as_view(), name='create_job_listing'),
]
