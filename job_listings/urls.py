from django.urls import path
from .views import JobListingList, JobListingCreate

urlpatterns = [
    path('', JobListingList.as_view(), name='job-listings-list'),
    path('api/listings/create/', JobListingCreate.as_view(), name='create_job_listing'),
]
