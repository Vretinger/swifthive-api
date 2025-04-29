from django.urls import path
from .views import (
    ApplyForJobAPI,
    ListUserApplicationsAPI,
    ListJobApplicationsAPI,
    UpdateApplicationStatusAPI
)

urlpatterns = [
    path("apply/", ApplyForJobAPI.as_view(), name="apply-for-job"),
    path("my/", ListUserApplicationsAPI.as_view(), name="my-applications"),
    path("<int:listing_id>/", ListJobApplicationsAPI.as_view(), name="job-applications"),
    path("<int:pk>/", UpdateApplicationStatusAPI.as_view(), name="update-application"),
]