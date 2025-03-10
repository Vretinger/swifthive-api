from django.urls import path
from .views import (
    ApplyForJobAPI,
    ListUserApplicationsAPI,
    ListJobApplicationsAPI,
    UpdateApplicationStatusAPI
)

urlpatterns = [
    path("applications/apply/", ApplyForJobAPI.as_view(), name="apply-for-job"),
    path("applications/my/", ListUserApplicationsAPI.as_view(), name="my-applications"),
    path("applications/<int:listing_id>/", ListJobApplicationsAPI.as_view(), name="job-applications"),
    path("applications/<int:id>/", UpdateApplicationStatusAPI.as_view(), name="update-application"),
]
